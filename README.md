
# Chicago Contract Spend Analysis

Procurement-style spend analysis of City of Chicago contract awards, 2023 to 2025 (work in progress).

Data: https://data.cityofchicago.org/d/rsxa-ify5 (download the CSV into data/contracts.csv)

- clean.py: cleans amounts, dates, vendor and department names, rolls up to one row per contract (11,408 contracts, $35.0B)
- Excel workbook (DataAnalysis.xlsx): pivot tables for supplier concentration, single-vendor risk by department, and contract size etc.

Findings:
Total vendors:	552
Top 10 share:	32%
Top 20 share:	44%
Vendors for 80% of spend:	91
% of vendors for 80%:	16%

Risk:
- 10 of 28 departments (over $1M spend, excluding UNKNOWN) have one vendor with 50%+ of spend
- Family and Support Services: 99.5% of $393M to Favorite Healthcare Staffing (5 vendors total) 
- Revenue: 84.8% of $56.8M to NTT Data (2 vendors) 
- Cultural Affairs and Special Events: 92% of $23.9M to Marquee Event Group 
- Aviation: 42.7% of $4.87B to AECOM Hunt / Clayco JV (biggest dept by far!!!) 
- merged 3 renamed departments (Fleet, Tech, Planning) 
- UNKNOWN dept = $267M with no department listed
