#!/usr/bin/env bash
set -e
# LAB_API_KEY is optional; uvicorn is already in the base image
exec uvicorn service_beta.main_v051:app --host 0.0.0.0 --port 8000 --workers 1
