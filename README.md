cat > README.md << 'EOF'
# Chicago Contract Spend Analysis

Procurement-style spend analysis of City of Chicago contract awards, 2023 to 2025 (work in progress).

Data: https://data.cityofchicago.org/d/rsxa-ify5 (download the CSV into data/contracts.csv)

- clean.py: cleans amounts, dates, vendor and department names, rolls up to one row per contract (11,408 contracts, $35.0B)
- Excel workbook (DataAnalysis.xlsx): pivot tables for supplier concentration, single-vendor risk by department, and contract size etc.
