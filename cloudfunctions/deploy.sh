#!/bin/bash
gcloud functions deploy scan_iac --runtime python310 --trigger-topic iac-files --region europe-west3
