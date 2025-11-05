resource "google_cloudfunctions_function" "dlp_function" {
  name        = "scan_iac"
  runtime     = "python310"
  entry_point = "scan_iac"
}
