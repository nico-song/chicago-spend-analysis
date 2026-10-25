import pandas as pd

df = pd.read_csv("data/contracts.csv", low_memory=False)
print("raw rows:", len(df))

cols = [
    "Purchase Order (Contract) Number",
    "Approval Date",
    "Department",
    "Contract Type",
    "Vendor Name",
    "Award Amount",
    "Procurement Type",
]
df = df[cols]
df = df.rename(columns={"Purchase Order (Contract) Number": "Contract ID"})

# money
df["Award Amount"] = df["Award Amount"].astype(str)
df["Award Amount"] = df["Award Amount"].str.replace("$", "", regex=False)
df["Award Amount"] = df["Award Amount"].str.replace(",", "", regex=False)
df["Award Amount"] = pd.to_numeric(df["Award Amount"], errors="coerce")

# dates
df["Approval Date"] = pd.to_datetime(df["Approval Date"], errors="coerce")
df["Year"] = df["Approval Date"].dt.year

# 2023 to 2025, no blank or $0 amounts
df = df[df["Year"] >= 2023]
df = df[df["Year"] <= 2025]
df = df[df["Award Amount"].notna()]
df = df[df["Award Amount"] != 0]
print("rows after filtering:", len(df))

# fill blanks
df["Department"] = df["Department"].fillna("UNKNOWN")
df["Contract Type"] = df["Contract Type"].fillna("UNKNOWN")
df["Procurement Type"] = df["Procurement Type"].fillna("UNKNOWN")
df["Vendor Name"] = df["Vendor Name"].fillna("UNKNOWN")

# merge renamed departments
df["Department"] = df["Department"].str.strip()
df["Department"] = df["Department"].replace({
    "PLANNING & DEVELOPMENT": "DEPARTMENT OF PLANNING AND DEVELOPMENT",
    "DEPT OF FLEET MGMT": "DEPARTMENT OF FLEET AND FACILITY MANAGEMENT",
    "DEPT OF INNOVATION & TECHNOLOGY": "DEPARTMENT OF TECHNOLOGY AND INNOVATION",
})

# clean vendor names
df["Vendor"] = df["Vendor Name"].str.upper()
df["Vendor"] = df["Vendor"].str.replace(".", "", regex=False)
df["Vendor"] = df["Vendor"].str.replace(",", "", regex=False)
df["Vendor"] = df["Vendor"].str.strip()
endings = r"\s+(INC|LLC|LLP|LTD|CORP|CORPORATION|CO|COMPANY)$"
df["Vendor"] = df["Vendor"].str.replace(endings, "", regex=True)
df["Vendor"] = df["Vendor"].str.replace(endings, "", regex=True)
df["Vendor"] = df["Vendor"].str.strip()
print("vendors before:", df["Vendor Name"].nunique())
print("vendors after:", df["Vendor"].nunique())

# spend by year, using every row so modifications count in the year they happened
yearly = df.groupby("Year").agg({"Award Amount": "sum"})
yearly = yearly.reset_index()
yearly.to_csv("output/yearly_spend.csv", index=False)
print(yearly)

# one row per contract
contracts = df.groupby("Contract ID").agg({
    "Award Amount": "sum",
    "Vendor": "first",
    "Department": "first",
    "Contract Type": "first",
    "Procurement Type": "first",
    "Year": "min",
})
contracts = contracts.reset_index()
contracts = contracts[contracts["Award Amount"] > 0]

print("contracts:", len(contracts))
print("total spend:", contracts["Award Amount"].sum())

contracts.to_csv("output/contracts_clean.csv", index=False)
print("saved")