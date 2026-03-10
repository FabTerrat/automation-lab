# API Data Extraction — Users

## Problem

Many tools expose data through APIs, but the raw responses are often complex JSON structures that are not directly usable by non-technical teams.

Teams frequently need a simple dataset (CSV / Excel) to analyze users, customers, or operational data.

Manually extracting this data is time-consuming and error-prone.

---

## Solution

This Python script automatically:

1. Calls a public API
2. Retrieves user data in JSON format
3. Extracts only the relevant fields
4. Generates a clean CSV dataset ready for analysis

The script demonstrates a common automation pattern:
API → Python → Structured dataset → CSV export


---

## Data Source

Public test API:

https://jsonplaceholder.typicode.com/users

---

## Extracted Fields

The script transforms the raw API response into a simplified dataset containing:

- `id`
- `name`
- `email`
- `company`
- `city`

Nested JSON fields are flattened for easier analysis.

---

## Output

The script generates:
users_export.csv

Example structure:
id,name,email,company,city
1,Leanne Graham,Sincere@april.biz,Romaguera-Crona,Gwenborough


---

## How to run

Install dependencies:
pip install -r requirements.txt

Run the script:
python script.py

---

## Project Structure
week-05_api
│
├ script.py
├ users_export.csv
├ requirements.txt
└ README.md

---

## Use Cases

Typical automation scenarios:

- Export data from SaaS tools
- Build reporting datasets
- Feed BI dashboards
- Prepare operational datasets