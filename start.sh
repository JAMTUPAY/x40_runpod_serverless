#!/usr/bin/env bash
set -e
# Your base image jamtupay/x40-lab:0.6 already contains the app and deps.
# This script just starts the same FastAPI server on port 8000.
exec uvicorn service_beta.main_v051:app --host 0.0.0.0 --port 8000 --workers 1
