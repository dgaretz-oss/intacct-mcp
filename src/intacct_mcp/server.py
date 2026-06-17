"""FastMCP server for the Sage Intacct REST API (with XML fallback).

Exposes per-category markdown references (under ``docs/rest/`` and ``docs/xml/``)
as MCP resources (``intacct://docs/{namespace}/{slug}``) AND as callable tools
(``list_docs`` / ``read_doc``) so they are reachable regardless of whether the
MCP client supports the resources/read protocol.

Intended workflow:
  1. Call ``list_docs()`` to discover available docs (REST by default).
  2. Call ``read_doc(slug)`` (or ``read_doc(slug, namespace="xml")``) for the
     relevant reference doc.
  3. Dispatch API calls via ``call_intacct`` / ``common_query`` (REST first).
  4. Only when REST genuinely cannot do the operation, fall back to
     ``call_xml_gateway``.

REST is the primary API. XML is a fallback for the small set of operations
that REST v1 does not yet cover (legacy transaction functions, post/unpost,
queries on XML-only objects, etc.). See the docstring on ``call_xml_gateway``
for guidance on when (and when NOT) to switch from REST to XML.

NOT AVAILABLE IN EITHER API: Financial Report Writer reports (Balance Sheet,
Income Statement, etc.), ``gl_fin`` / ``gl_tb`` exports, and financial graphs.
Both REST and XML lack a run path for these — they must be generated from the
Intacct UI or scheduled to SFTP/cloud storage.
"""

from __future__ import annotations

import pathlib
from datetime import datetime, timezone

from dotenv import find_dotenv, load_dotenv
from mcp.server.fastmcp import FastMCP

from intacct_mcp import auth, xml_gateway
from intacct_mcp.client import get_client
from intacct_mcp.xml_gateway import XmlGatewayConfigError, XmlGatewayError

# Locate .env by searching upward from CWD first (portable; works on any
# device regardless of where the package is installed), then fall back to the
# path relative to this file as a secondary hint.
_DOTENV_PATH = find_dotenv(usecwd=True) or str(
    pathlib.Path(__file__).resolve().parent.parent.parent / ".env"
)
load_dotenv(_DOTENV_PATH)

mcp = FastMCP(
    "Intacct MCP",
    instructions=(
        "MCP server for the Sage Intacct REST API, with an XML gateway fallback.\n\n"
        "ALWAYS PREFER REST. The XML fallback is for narrow cases where REST v1\n"
        "genuinely does not expose the operation -- not as a retry for malformed\n"
        "REST requests. Most REST errors are caused by bad payload shape, missing\n"
        "fields, or wrong path. Diagnose the REST error first.\n\n"
        "QUERY PATTERN -- always use common_query or POST services/core/query:\n"
        "  - Filters use MongoDB-style $-prefix operators: {\"$eq\": {\"fieldName\": \"value\"}}\n"
        "  - String match: {\"$like\": {\"fieldName\": \"%value%\"}}\n"
        "  - Null check:   {\"$isNull\": \"fieldName\"}\n"
        "  - orderBy format: [{\"fieldName\": \"desc\"}]\n"
        "  - Pagination: size (max 4000) and start (1-based) in the request body\n"
        "  - Multi-condition filters: filterExpression \"(1 and 2) or 3\" (1-based index)\n"
        "  - filterParameters: {\"caseSensitiveComparison\": false} for case-insensitive\n\n"
        "WHAT WORKS (REST):\n"
        "  POST services/core/query  -- filtered/sorted/paginated queries\n"
        "  GET  objects/<resource>/{key}  -- single record, full fields\n"
        "  GET  objects/<resource>        -- key list only, no filter/sort\n"
        "  GET  services/core/model?name=<resource>  -- field schema discovery\n"
        "  GET  objects/<resource>/id1,id2,id3  -- batch GET up to 500 records\n\n"
        "HEADERS (pass via call_intacct headers= param):\n"
        "  Atomic batch:  {\"X-IA-API-ParamTransaction\": \"true\"}\n"
        "  Async request: {\"Prefer\": \"respond-async\"}\n"
        "  Idempotency:   {\"Idempotency-Key\": \"<unique-key>\"}\n"
        "  Entity target: {\"X-IA-API-ParamEntity\": \"<entity-id>\"}\n"
        "  NOTE: X-IA-API-ParamEntity is IGNORED by the report service.\n"
        "  For reports, use parameters.dimensions.location.id in the body.\n\n"
        "REPORTS (Custom Report Writer reports only; async submit/poll/download):\n"
        "  run_report(application_name, report_name, name, output_type, parameters)\n"
        "  report_status(report_id, output_type, output_location)\n"
        "  cancel_report(report_id, output_type, output_location)\n"
        "  Download: call_intacct GET services/reports/download?reportId=X&outputType=Y\n\n"
        "FINANCIAL REPORTS ARE NOT AVAILABLE IN EITHER API:\n"
        "  Balance Sheet, Income Statement, Statement of Cash Flows, FRW reports,\n"
        "  gl_fin/gl_tb exports, and financial graphs CANNOT be retrieved via\n"
        "  REST or XML. Tell the user up front; do not retry with XML. They must\n"
        "  be run from the Intacct UI or scheduled to SFTP/cloud storage.\n\n"
        "OWNED OBJECTS (e.g. bill-line owned by bill):\n"
        "  POST objects/accounts-payable/bill with \"lines\": [...] -- create owner+lines\n"
        "  PATCH objects/accounts-payable/bill/{key} lines: include key=update, omit key=add\n"
        "  lines: [{\"ia::operation\":\"delete\",\"key\":\"7200\"},...] -- mixed add/update/delete\n"
        "  POST objects/accounts-payable/bill-line with \"bill\":{\"key\":\"901\"} -- direct create\n\n"
        "BULK JOBS (large async batches, no record limit):\n"
        "  bulk_submit_job(object_name, operation, records) -- submit, get jobId\n"
        "  bulk_job_status(job_id) -- poll status; set download=True when completed\n\n"
        "ASYNC REQUESTS (Prefer: respond-async header):\n"
        "  Pass headers={\"Prefer\": \"respond-async\"} to call_intacct\n"
        "  Receive 202 ACK with jobId; then poll:\n"
        "  async_job_status(job_id) -- returns state: queued/inTransit/delivered/dead\n\n"
        "XML FALLBACK -- call_xml_gateway (USE SPARINGLY):\n"
        "  Switch to XML ONLY when there is a confirmed REST gap:\n"
        "    - Legacy transaction functions (create_sotransaction, create_bill on\n"
        "      transactions REST does not expose, create_invoice variants, etc.)\n"
        "    - readByQuery on XML-ONLY objects (see docs/xml/xml-only-objects.md)\n"
        "    - Post/unpost or specialized state transitions not exposed via REST\n"
        "    - Legacy attachment/document workflows missing from REST\n"
        "  Do NOT use as a retry for malformed REST -- fix the REST request first.\n"
        "  Requires INTACCT_SENDER_ID / INTACCT_SENDER_PASSWORD env vars.\n\n"
        "WHAT DOES NOT WORK:\n"
        "  POST services/query       -- blocked (use services/core/query instead)\n"
        "  POST common/bulk-requests -- wrong endpoint, does not exist\n"
        "  Query string params on GET /objects/... -- not supported\n"
        "  Financial Report Writer reports via API -- NOT available in REST or XML\n\n"
        "Run get_credentials_status and test_connection first if authentication "
        "is uncertain.\n\n"
        "DOCS: Use list_docs() to see REST reference docs, list_docs(namespace=\"xml\")\n"
        "for XML, or list_docs(namespace=\"all\") for both. Then read_doc(slug) for\n"
        "REST docs or read_doc(slug, namespace=\"xml\") for XML docs. Do NOT use\n"
        "call_intacct or intacct:// URIs to access docs."
    ),
)

# docs/ lives at the project root and is split into rest/ and xml/ subfolders.
DOCS_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent / "docs"
DOCS_PATHS: dict[str, pathlib.Path] = {
    "rest": DOCS_ROOT / "rest",
    "xml": DOCS_ROOT / "xml",
}


def _list_slugs(namespace: str) -> list[str]:
    path = DOCS_PATHS.get(namespace)
    if path is None or not path.is_dir():
        return []
    return sorted(p.stem for p in path.glob("*.md"))


def _resolve_doc(slug: str, namespace: str) -> pathlib.Path | None:
    path = DOCS_PATHS.get(namespace)
    if path is None:
        return None
    doc = path / f"{slug}.md"
    return doc if doc.exists() else None


# --- Resources: one markdown reference per category -----------------------
def _register_doc_resources() -> None:
    """Register every docs/{rest,xml}/*.md file as a separate resource."""
    for namespace, path in DOCS_PATHS.items():
        if not path.is_dir():
            continue
        for doc_file in sorted(path.glob("*.md")):
            slug = doc_file.stem
            title = f"{namespace.upper()} {slug.replace('-', ' ').title()}"

            def make_resource(p: pathlib.Path, ns: str) -> None:
                uri = f"intacct://docs/{ns}/{p.stem}"

                @mcp.resource(
                    uri,
                    name=f"Intacct docs ({ns}): {p.stem}",
                    description=(
                        f"Sage Intacct {ns.upper()} API reference for {title}. "
                        "Lists endpoints/functions, required fields, and "
                        "request/response examples for this category. Read this "
                        f"before constructing a {'call_intacct' if ns == 'rest' else 'call_xml_gateway'} "
                        "request for this category."
                    ),
                    mime_type="text/markdown",
                )
                def _resource() -> str:
                    return p.read_text(encoding="utf-8")

            make_resource(doc_file, namespace)


_register_doc_resources()


# --- Doc tools (tool-accessible mirror of the MCP resources) --------------

@mcp.tool()
def list_docs(namespace: str = "rest") -> dict:
    """List Intacct reference doc slugs.

    The docs folder is split into two namespaces:
      - "rest" -- REST v1 API docs (default; use these for call_intacct /
                  common_query). Includes rest-only-objects.md listing objects
                  that exist ONLY in REST.
      - "xml"  -- XML gateway docs (use these for call_xml_gateway). Includes
                  xml-only-objects.md listing objects that exist ONLY in XML
                  and functions.md describing the legacy function model.
      - "all"  -- Both namespaces.

    Args:
        namespace: "rest" (default), "xml", or "all".

    Returns:
        Dict with a "docs" list of slugs. For namespace="all", returns
        {"rest": [...], "xml": [...]}.
    """
    if namespace == "all":
        return {
            "rest": _list_slugs("rest"),
            "xml": _list_slugs("xml"),
        }
    if namespace not in DOCS_PATHS:
        return {
            "docs": [],
            "error": f"Unknown namespace '{namespace}'. Use 'rest', 'xml', or 'all'.",
        }
    return {"namespace": namespace, "docs": _list_slugs(namespace)}


@mcp.tool()
def read_doc(slug: str, namespace: str = "rest") -> str:
    """Read an Intacct reference doc by slug name.

    Use list_docs() first to see all available slugs. Read the relevant doc
    before constructing any call_intacct/common_query (REST) or call_xml_gateway
    (XML) request for that category -- it contains endpoint paths, required
    fields, and examples.

    Useful REST slugs (namespace="rest", the default):
      accounts-payable          -- bills, vendors, payments
      accounts-receivable       -- invoices, customers, receipts
      general-ledger            -- journal entries, accounts, GL batches
      order-entry               -- sales orders, invoices, shipments
      purchasing                -- purchase orders, receipts, returns
      query-service             -- full query syntax, operators, pagination
      owner-and-owned-objects   -- bill-line / owned object patterns
      reports-service           -- async report submission and polling (CRW only)
      intacct-report-entity-filter -- entity filtering for reports (location.id)
      http-headers              -- all supported request/response headers
      error-handling            -- HTTP status codes, ia::error shape
      async-requests            -- Prefer: respond-async pattern
      bulk-requests             -- bulk jobs, composite requests
      rest-only-objects         -- objects that exist ONLY in REST (no XML)

    Useful XML slugs (namespace="xml"):
      xml-only-objects          -- 366 objects that exist ONLY in XML
      functions                 -- XML generic vs. legacy/object-specific funcs
      accounts-payable-bills    -- XML create_bill, update_bill, etc.
      order-entry-order-entry-transactions -- create_sotransaction etc.
      <module-object>           -- one .md per object/module
                                   (e.g. contracts-rev-mgmt-contracts)

    Args:
        slug:      Doc name without extension, e.g. "accounts-payable".
                   Use list_docs(namespace=...) if unsure.
        namespace: "rest" (default) or "xml".

    Returns:
        Full markdown content of the requested doc, or an error message with
        available slugs if not found.
    """
    if namespace not in DOCS_PATHS:
        return (
            f"Unknown namespace '{namespace}'. Use 'rest' or 'xml'.\n"
            "Try list_docs(namespace='all') to see what is available."
        )
    doc_path = _resolve_doc(slug, namespace)
    if doc_path is None:
        available = _list_slugs(namespace)
        return (
            f"Doc '{slug}' not found in '{namespace}'. Available slugs:\n"
            + "\n".join(f"  {s}" for s in available)
        )
    return doc_path.read_text(encoding="utf-8")


# --- Tools ----------------------------------------------------------------
@mcp.tool()
async def call_intacct(
    method: str,
    path: str,
    params: dict = {},
    body: dict = {},
    headers: dict = {},
) -> dict:
    """Execute any Sage Intacct REST API request.

    Read the relevant doc with read_doc(slug) first to find the correct path,
    required fields, and expected response shape for your operation.

    Useful paths:
      GET  objects/<resource>          -- list keys (no filter/sort support)
      GET  objects/<resource>/{key}    -- single record with all fields
      GET  objects/<resource>/k1,k2,k3 -- batch GET up to 500 records
      POST services/core/query         -- filtered, sorted, paginated queries
      POST services/core/composite     -- 2-10 sub-requests in one call
      GET  services/core/model         -- object schema and field names
        e.g. GET services/core/model?name=accounts-payable/bill

    Common headers:
      Atomic batch:  {"X-IA-API-ParamTransaction": "true"}
      Async:         {"Prefer": "respond-async"}
        Returns 202 ACK with jobId; poll with async_job_status()
      Idempotency:   {"Idempotency-Key": "<uuid>"}  (POST/PATCH only; cached 48h)
      Entity target: {"X-IA-API-ParamEntity": "<entity-id>"}

    Args:
        method:  HTTP method - GET, POST, PATCH, or DELETE.
        path:    API path relative to base URL, without leading slash, e.g.
                 "objects/accounts-payable/vendor/42".
        params:  Query string parameters (used for GET requests).
        body:    Request body for POST/PATCH requests.
        headers: Additional HTTP headers merged with auth headers.

    Returns:
        Parsed JSON response from Intacct, including ia::result and ia::meta.
        Async requests return 202 ACK with jobId instead of the final result.
    """
    client = get_client()
    return await client.request(
        method, path, params=params, body=body,
        extra_headers=headers or None,
    )


@mcp.tool()
async def common_query(
    object: str,
    fields: list[str] = [],
    filters: list[dict] = [],
    filter_expression: str = "",
    order_by: list[dict] = [],
    filter_parameters: dict = {},
    size: int = 10,
    start: int = 1,
) -> dict:
    """Query any Intacct object using the POST /services/core/query endpoint.

    Supports field selection, filtering with boolean expressions, sorting,
    and pagination. See read_doc("query-service") for the full reference.

    FILTER FORMAT -- MongoDB-style $-prefixed operators, field name is the key inside:
      Equal         -- {"$eq":  {"state": "posted"}}
      Not equal     -- {"$ne":  {"state": "paid"}}
      Greater than  -- {"$gt":  {"totalTxnAmountDue": 0}}
      Less than     -- {"$lt":  {"totalTxnAmountDue": 1000}}
      Gte           -- {"$gte": {"txnDate": "2024-01-01"}}
      Lte           -- {"$lte": {"txnDate": "2024-12-31"}}
      In list       -- {"$in":  {"state": ["posted", "partiallyPaid"]}}
      Like          -- {"$like":{"vendorName": "%acme%"}}
      Is null       -- {"$isNull": "fieldName"}

    Multi-condition example:
      filters = [
        {"$eq": {"state": "posted"}},
        {"$gt": {"totalTxnAmountDue": 0}}
      ]
      filter_expression = "1 and 2"

    Complex AND/OR: filterExpression uses 1-based filter indexes with parens:
      filter_expression = "(1 and 2) or 3"

    Dot notation for related object fields:
      fields = ["key", "id", "vendor.id", "vendor.name"]
      object = "accounts-payable/bill-line" can include "bill.id", "bill.postingDate"

    Aggregate functions in fields:
      "sum:totalDue", "avg:totalDue", "min:txnDate", "max:txnDate", "count:status"
      Non-aggregate fields become implicit GROUP BY fields.

    orderBy format -- {"fieldName": "asc"|"desc"}, one field per dict:
      order_by = [{"totalTxnAmountDue": "desc"}, {"dueDate": "asc"}]

    filterParameters options:
      {"caseSensitiveComparison": false}  -- case-insensitive string comparisons
      {"includePrivate": true}            -- include private records (top-level only)
      {"asOfDate": "2024-06-01"}          -- anchor date for relative date values

    Pagination: start is 1-based. ia::meta.next is null when on the last page.
      Page through: start=1 → next page start = previous_start + size → repeat.

    Args:
        object:            Object path, e.g. "accounts-payable/bill". Supports
                           document type notation: "order-entry/document::Sales Invoice"
                           and custom type: "accounts-payable/vendor::CRE Partner".
        fields:            Field names to return. Supports dot-notation for related
                           fields. Use "sum:field" etc. for aggregates.
        filters:           List of filter dicts using {field, operator, value} format.
        filter_expression: Boolean expression over filter indexes (1-based),
                           e.g. "1 and 2" or "(1 and 2) or 3". Only needed
                           when combining filters with OR or complex logic.
        order_by:          Sort order. Each dict maps one field to "asc"/"desc".
        filter_parameters: Optional dict: caseSensitiveComparison, includePrivate,
                           asOfDate.
        size:              Number of records per page (default 10, max 4000).
        start:             1-based offset for pagination (default 1).

    Returns:
        ia::result array of matching objects and ia::meta with totalCount and next.

    Known valid state values for accounts-payable/bill:
        draft | submitted | partiallyApproved | declined | posted |
        selected | paid | partiallyPaid | reversed | reversal |
        analyzing | noValue
    """
    client = get_client()
    body: dict = {
        "object": object,
        "size": size,
        "start": start,
    }
    if fields:
        body["fields"] = fields
    if filters:
        body["filters"] = filters
    if filter_expression:
        body["filterExpression"] = filter_expression
    if order_by:
        body["orderBy"] = order_by
    if filter_parameters:
        body["filterParameters"] = filter_parameters
    return await client.request("POST", "services/core/query", body=body)


@mcp.tool()
async def call_xml_gateway(
    function_xml: str,
    control_id: str = "",
    transaction: bool = False,
    parse: bool = True,
) -> dict:
    """Fallback tool: POST a raw XML function to the Intacct legacy XML gateway.

    USE THIS ONLY WHEN REST GENUINELY CANNOT DO THE JOB.
    Most REST errors are caused by bad payload shape, missing required fields,
    or the wrong path -- NOT by a real REST limitation. Do NOT switch to XML on
    the first REST error. Read the relevant REST doc, fix the request, and
    only fall back to XML when you have evidence of a real gap.

    Genuine reasons to use XML:
      1. Legacy transaction functions (no REST equivalent yet):
         create_sotransaction, update_sotransaction, create_potransaction,
         create_ictransaction, create_invoice (some types), create_bill (some
         types), update_<legacy_txn>.
      2. readByQuery / read / get_list against an XML-ONLY object:
         see docs/xml/xml-only-objects.md (366 objects, including most
         primary-doc / detail records and many APRECORD / ARRECORD variants).
      3. Specialized business actions not exposed in REST:
         post / unpost, document stage conversion, certain approval workflows,
         legacy inventory/order-management actions.
      4. Legacy attachment and supporting-document workflows that have no
         REST equivalent.

    NOT a reason to use XML:
      - REST returned 400, 404, or "object not found" -- first verify the object
        is not in docs/rest/rest-only-objects.md, check spelling/path, and call
        services/core/model for the correct field schema. Many "REST gaps" are
        actually wrong object names or missing fields.
      - REST returned 403 -- this is permissions; XML will fail too.
      - The user wants a Financial Report Writer report (Balance Sheet, Income
        Statement, Statement of Cash Flows, gl_fin, gl_tb, financial graph,
        etc.). FRW reports CANNOT be retrieved via REST or XML. Tell the user
        they must be generated from the Intacct UI or scheduled to SFTP/cloud
        storage. Do not attempt the XML fallback for these.

    Configuration:
      Requires INTACCT_SENDER_ID and INTACCT_SENDER_PASSWORD in your .env.
      These are the Web Services sender credentials used by the legacy XML
      gateway's outer firewall envelope. Get them from your Intacct admin
      (Company > Setup > Web Services Sender IDs). No new USER credentials
      are needed -- the existing OAuth bearer is exchanged for an XML session
      ID under the hood via the REST endpoint GET services/core/session/id.

    Args:
        function_xml: The XML body of the legacy function. May be either:
                      (a) just the function content, e.g.
                          "<readByQuery><object>APRECORD</object>
                           <fields>*</fields><query>STATE='posted'</query>
                           <pagesize>200</pagesize></readByQuery>"
                          -- the tool will wrap it in <function controlid=...>.
                      (b) the full <function ...>...</function> element if you
                          want to set the controlid attribute yourself.
                      Multiple <function> blocks can be concatenated for a
                      batch request (use transaction=True for all-or-nothing).
        control_id:   Optional control ID for the request envelope and the
                      wrapper <function>. Generated if omitted.
        transaction:  If True, treat the operation as atomic -- if any function
                      fails, all are rolled back. Useful for multi-function
                      writes.
        parse:        If True (default), parse the XML response into a dict.
                      If False, return the raw XML string.

    Returns:
        On success:
          parse=True:  {"status": "success", "parsed_response": {...}}
          parse=False: {"status": "success", "xml_response": "<response>..."}
        On failure:
          {"status": "error", "level": "...", "description": "...",
           "parsed_response"/"raw_response": ...}
        On config error (missing sender env vars):
          {"status": "config_error", "message": "..."}

    Examples:
      # readByQuery on an XML-only object (AP detail records)
      await call_xml_gateway(
          "<readByQuery><object>APRECORD</object><fields>*</fields>"
          "<query>STATE='posted'</query><pagesize>200</pagesize></readByQuery>"
      )

      # Post a legacy sales-order transaction
      await call_xml_gateway(
          "<create_sotransaction transactiontype='Sales Order'>"
          "  <datecreated><year>2026</year><month>03</month><day>31</day></datecreated>"
          "  <customerid>CUST-001</customerid>"
          "  <sotransitems>"
          "    <sotransitem>"
          "      <itemid>WIDGET-A</itemid>"
          "      <quantity>10</quantity>"
          "    </sotransitem>"
          "  </sotransitems>"
          "</create_sotransaction>"
      )
    """
    try:
        return await xml_gateway.post_xml(
            function_xml=function_xml,
            control_id=control_id or None,
            transaction=transaction,
            parse=parse,
        )
    except XmlGatewayConfigError as exc:
        return {
            "status": "config_error",
            "message": str(exc),
            "hint": (
                "Add INTACCT_SENDER_ID and INTACCT_SENDER_PASSWORD to your .env "
                "file. They are only required for call_xml_gateway -- REST "
                "operations continue to work without them."
            ),
        }
    except XmlGatewayError as exc:
        return {
            "status": "error",
            "message": str(exc),
            "raw_response": getattr(exc, "raw_response", ""),
        }


@mcp.tool()
async def bulk_submit_job(
    object_name: str,
    operation: str,
    records: list[dict],
    callback_url: str = "",
) -> dict:
    """Submit an asynchronous bulk create/update/delete job.

    Intacct processes bulk jobs asynchronously via multipart form upload.
    This call returns immediately with a jobId -- poll with bulk_job_status().

    Each job targets a single object type and a single operation. Submit
    separate jobs for different objects or operations.

    Args:
        object_name:  Full object path, e.g. "accounts-payable/vendor" or
                      "general-ledger/journal-entry".
        operation:    One of "create", "update", or "delete".
        records:      List of record dicts to process. For "create", include
                      all required fields. For "update"/"delete", include "key"
                      or "id" to identify each record.
        callback_url: Optional HTTPS URL Intacct will POST results to when
                      the job completes.

    Returns:
        ia::result with jobId and statusURL for polling.
        Example: {"jobId": "950bf10d-...", "statusURL": "/services/bulk/job/status?jobId=..."}
    """
    import json as _json

    client = get_client()

    # The bulk endpoint requires multipart/form-data with two fields:
    #   ia::requestBody -- JSON string describing the job
    #   file            -- the JSON array of records as a file upload
    request_body_obj: dict = {
        "objectName": object_name,
        "operation": operation,
        "jobFile": "records.json",
        "fileContentType": "json",
    }
    if callback_url:
        request_body_obj["callbackURL"] = callback_url

    file_bytes = _json.dumps(records).encode("utf-8")

    multipart = {
        "ia::requestBody": (None, _json.dumps(request_body_obj), "application/json"),
        "file": ("records.json", file_bytes, "application/json"),
    }

    return await client.request(
        "POST", "services/bulk/job/create", multipart=multipart
    )


@mcp.tool()
async def bulk_job_status(
    job_id: str,
    download: bool = False,
) -> dict:
    """Check the status of an async bulk job submitted with bulk_submit_job.

    Poll this until status is "completed" or "failed". Once completed,
    set download=True to retrieve the full results file containing per-record
    success/error details.

    Args:
        job_id:   The jobId returned by bulk_submit_job.
        download: Set True after status is "completed" to download results.

    Returns:
        ia::result with jobId, status, percentComplete, and (when complete)
        downloadURL and jobStatusFile.
        Status values: "queued" | "processing" | "completed" | "failed"
    """
    client = get_client()
    params: dict = {"jobId": job_id}
    if download:
        params["download"] = "true"
    return await client.request("GET", "services/bulk/job/status", params=params)


@mcp.tool()
async def async_job_status(job_id: str) -> dict:
    """Check the status of an async request submitted with Prefer: respond-async.

    This is for jobs created by passing {"Prefer": "respond-async"} in the
    headers of a call_intacct call. It is NOT for bulk jobs -- use
    bulk_job_status() for those.

    When an async request is accepted, Intacct returns HTTP 202 with a jobId
    and an href. Pass that jobId here to poll for delivery status.

    States:
      queued    -- Job is waiting in the queue.
      inTransit -- Job is currently processing.
      delivered -- Job completed; response was sent to the webhook.
      dead      -- Job failed or expired.
      cancelled -- Job was manually cancelled.
      deferred  -- Job delayed for later processing.

    Job status details are available for 4 days after completion. The status
    endpoint returns delivery state only -- the actual result is sent to the
    webhook specified via X-IA-Webhook-EndpointURL or X-IA-Webhook-Id at
    request time.

    Args:
        job_id: The base64url-encoded jobId from the 202 ACK response.

    Returns:
        ia::result with jobId, state, queuedDateTime, and deliveryStatus.
    """
    client = get_client()
    return await client.request(
        "GET",
        "services/core/async/job-status",
        params={"jobId": job_id},
    )


@mcp.tool()
async def run_report(
    application_name: str,
    report_name: str,
    name: str,
    output_type: str = "csv",
    output_location: str = "intacct",
    parameters: dict = {},
) -> dict:
    """Submit a Custom Report Writer (CRW) report for async processing.

    SCOPE: This tool runs Custom Report Writer (CRW) reports only.
    Financial Report Writer (FRW) reports -- Balance Sheet, Income Statement,
    Statement of Cash Flows, gl_fin, gl_tb, financial graphs -- CANNOT be run
    via REST OR XML. Tell the user up front and direct them to the Intacct UI
    or a scheduled SFTP/cloud delivery. Do not fall back to call_xml_gateway
    for FRW reports.

    Reports are processed asynchronously -- this call returns immediately with
    a reportId and status "submitted". The report may take anywhere from
    seconds to several minutes depending on complexity and data volume.

    IMPORTANT -- after calling this tool, Claude should:
    1. Tell the user the report has been queued and share the reportId.
    2. Explain that report generation can take a few seconds to several minutes.
    3. Offer to check status when the user is ready (via report_status()).
    4. Do NOT poll in a loop or block waiting -- return control to the user.

    ENTITY / LOCATION FILTERING (critical):
    The X-IA-API-ParamEntity header is IGNORED by the report service. To scope
    a report to a specific entity/location, pass the location ID in the body:
      parameters = {"dimensions": {"location": {"id": "102"}}}

    TIME PERIOD PARAMETERS:
    For date-range reports (Trial Balance, Account Balance):
      parameters = {
        "timePeriod": {"dateRange": {"startDate": "2026-03-01",
                                      "endDate": "2026-03-31"}}
      }
    For point-in-time reports (Balance Sheet):
      parameters = {
        "timePeriod": {"periodToDate": {"asOfDate": "2026-03-31"}}
      }

    STATISTICAL ACCOUNTS:
    By default, statistical accounts are excluded. Add to parameters:
      "showStatisticalAccounts"       -- include alongside regular
      "onlyShowStatisticalAccounts"   -- statistical only
      "doNotShowStatisticalAccounts"  -- exclude (default)

    CONFIRMED WORKING REPORT SLUGS (general-ledger namespace):
      general-ledger/trial-balance    -- timePeriod.dateRange
      general-ledger/account-balance  -- timePeriod.dateRange or periodToDate
                                         also requires glAccountRange or
                                         glAccountGroup

    KNOWN LIMITATION -- Financial reports:
    The "financial-reports" namespace (services/reports/financial-reports/...)
    is not enabled in REST v1. The XML gateway does NOT expose them either.
    Balance Sheet / Income Statement / Statement of Cash Flows must be run
    from the Intacct UI or delivered via SFTP/cloud storage on a schedule.

    Args:
        application_name: Application namespace, e.g. "general-ledger".
        report_name:      Report slug, e.g. "trial-balance".
        name:             Display label for this report run.
        output_type:      "html", "pdf", "csv", "excel", or "text".
        output_location:  "intacct" (default) or "cloud".
        parameters:       Report-specific parameters dict.

    Returns:
        202 ACK with reportId, status ("submitted"), and href for polling.
    """
    client = get_client()
    body: dict = {
        "name": name,
        "outputType": output_type,
        "outputLocation": output_location,
    }
    if parameters:
        body["parameters"] = parameters
    path = f"services/reports/{application_name}/{report_name}"
    return await client.request("POST", path, body=body)


@mcp.tool()
async def report_status(
    report_id: str,
    output_type: str,
    output_location: str = "intacct",
) -> dict:
    """Check the status of a report job submitted with run_report.

    Status values: "pending" | "completed" | "canceled" | "failed".

    IMPORTANT -- how Claude should handle each status:
      "pending":   Tell the user the report is still running and to check back
                   in a minute. Do NOT call this tool again immediately in a
                   loop -- return control to the user.
      "completed": Proceed to download via call_intacct GET on the downloadURL.
      "failed":    Report the error details to the user.

    When completed with outputLocation "intacct", the response includes a
    downloadURL -- fetch it with: call_intacct("GET", downloadURL).

    Args:
        report_id:       The reportId from the run_report response.
        output_type:     "html","pdf","csv","excel","text".
        output_location: "intacct" or "cloud".

    Returns:
        ia::result with status and, when completed, downloadURL.
    """
    client = get_client()
    return await client.request(
        "GET",
        "services/reports/status",
        params={
            "reportId": report_id,
            "outputType": output_type,
            "outputLocation": output_location,
        },
    )


@mcp.tool()
async def cancel_report(
    report_id: str,
    output_type: str,
    output_location: str = "intacct",
) -> dict:
    """Cancel a queued report job.

    Only queued (submitted) reports can be canceled; in-progress reports
    cannot.

    Args:
        report_id:       The reportId from the run_report response.
        output_type:     "html","pdf","csv","excel","text".
        output_location: "intacct" or "cloud".

    Returns:
        ia::result with status "canceled" on success.
    """
    client = get_client()
    return await client.request(
        "POST",
        "services/reports/cancel",
        body={
            "reportId": report_id,
            "outputType": output_type,
            "outputLocation": output_location,
        },
    )


@mcp.tool()
def get_credentials_status() -> dict:
    """Report which credentials are configured, without exposing any values.

    Returns:
      - REST OAuth credentials: client id/secret loaded, base URL, token cache.
      - XML fallback credentials: whether INTACCT_SENDER_ID and
        INTACCT_SENDER_PASSWORD are present. These are only required for
        call_xml_gateway; REST works without them.
    """
    status = auth.get_credentials_status()
    status["xml_fallback"] = xml_gateway.config_status()
    return status


@mcp.tool()
async def test_connection() -> dict:
    """Confirm REST authentication and connectivity with a lightweight request.

    Probes GET services/core/model?name=accounts-payable/bill -- a read-only
    schema endpoint accessible to all API users. Returns success/failure with
    a UTC timestamp.

    A 403 on this call is a real auth/permissions failure.

    This tool only checks REST connectivity. The XML fallback uses the same
    OAuth token exchanged for an XML session ID -- confirm sender credentials
    are loaded via get_credentials_status() if you plan to use
    call_xml_gateway.
    """
    client = get_client()
    try:
        result = await client.request(
            "GET",
            "services/core/model",
            params={"name": "accounts-payable/bill"},
        )
        return {
            "status": "success",
            "response": result,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "error",
            "message": str(exc),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }


def main() -> None:
    """Entry point for the ``intacct-mcp`` console script.

    Sub-commands
    ------------
    login
        Open a browser to log in via OAuth 2.0 Authorization Code + PKCE and
        save the resulting tokens to ``~/.intacct_mcp_tokens.json``.

    (no sub-command)
        Start the MCP server (default).
    """
    import sys

    args = sys.argv[1:]

    if args and args[0] == "login":
        from intacct_mcp.login import run_login_flow

        run_login_flow()
        return

    mcp.run()


if __name__ == "__main__":
    main()
