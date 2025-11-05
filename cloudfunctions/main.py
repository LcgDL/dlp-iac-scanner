import json
import re
from google.cloud import dlp_v2, pubsub_v1, bigquery

def scan_iac(event, context):
    data = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    file_content = data.get("content", "")
    project_id = "your-gcp-project"

    dlp = dlp_v2.DlpServiceClient()
    parent = f"projects/{project_id}"

    # Beispiel: einfache DLP-Erkennung
    item = {"value": file_content}
    response = dlp.inspect_content(
        request={"parent": parent, "item": item, "inspect_config": {"include_quote": True}}
    )

    findings = [f.quote for f in response.result.findings]
    bq_client = bigquery.Client()
    table_id = f"{project_id}.dlp_results.findings"

    errors = bq_client.insert_rows_json(table_id, [{"findings": findings}])
    if errors:
        print(f"Fehler beim Schreiben in BigQuery: {errors}")

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, "dlp-alerts")
    publisher.publish(topic_path, data=json.dumps(findings).encode("utf-8"))
