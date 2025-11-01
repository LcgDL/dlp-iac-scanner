# Serverless DLP Scanner for IaC (Terraform) on GCP

This project demonstrates how to build a **serverless DLP scanning pipeline** that analyzes Infrastructure-as-Code (IaC) files (e.g., Terraform) for **sensitive data** such as secrets, passwords, or API keys using **Google Cloud DLP, Cloud Functions, Pub/Sub, and BigQuery**.

## Overview

**Goal:** Automate security checks for Terraform configurations and detect potential data leaks or secret exposures.

### Components
| Component | Technology | Purpose |
|------------|-------------|----------|
| Cloud Function | Python + google-cloud-dlp | Scan IaC for secrets |
| BigQuery | Data Storage | Store DLP scan results |
| Pub/Sub | Messaging | Trigger alerts on high-risk findings |
| Cloud Build | CI/CD | Automate Terraform security checks |
| Looker Studio | Visualization | Dashboard for DLP results |

## Data Flow
1. Developer uploads a Terraform file to a GCS bucket.
2. A Cloud Function is triggered by the upload event.
3. The function scans the file using:
   - **Cloud DLP API**
   - **Regex patterns**
   - **Terraform SDK validation**
4. Results are stored in **BigQuery**.
5. High-risk findings trigger **Pub/Sub alerts**.
6. **Cloud Build** runs additional Terraform security checks.
7. Results can be visualized in **Looker Studio**.

---

## Local Testing
```bash
cd cloudfunctions
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
