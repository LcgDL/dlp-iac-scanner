resource "google_bigquery_dataset" "dlp_results" {
  dataset_id = "dlp_results"
  location  = var.region
}

resource "google_bigquery_table" "dlp_results" {
  dataset_id = google_bigquery_dataset.dlp_results.dataset_id
  table_id   = "findings"
  schema     = jsonencode([{"name":"findings","type":"STRING","mode":"REPEATED"}])
}
