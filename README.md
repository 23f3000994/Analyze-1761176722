# Web App

This is a minimal web app that processes data from an Excel file and generates a CSV.

## Setup

1. Ensure you have Python 3.11+ and Pandas 2.3 installed.
2. Run `python execute.py` to generate `data.csv`.

## CI

This project uses GitHub Actions for continuous integration. The workflow runs ruff and executes the script to generate `result.json`.