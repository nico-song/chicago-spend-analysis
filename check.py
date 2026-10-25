import pandas as pd

# check 1: biggest contracts in 2023
clean = pd.read_csv("output/contracts_clean.csv")
c2023 = clean[clean["Year"] == 2023]
print(c2023.sort_values("Award Amount", ascending=False).head(10))

# check 2 and 3: raw data by year
raw = pd.read_csv("data/contracts.csv")
raw["Approval Date"] = pd.to_datetime(raw["Approval Date"], errors="coerce")
raw["Year"] = raw["Approval Date"].dt.year

raw["Award Amount"] = raw["Award Amount"].astype(str)
raw["Award Amount"] = raw["Award Amount"].str.replace("$", "", regex=False)
raw["Award Amount"] = raw["Award Amount"].str.replace(",", "", regex=False)
raw["Award Amount"] = pd.to_numeric(raw["Award Amount"], errors="coerce")

print("all raw rows by year:")
print(raw["Year"].value_counts().sort_index().tail(6))

zero = raw[raw["Award Amount"] == 0]
print("$0 rows by year:")
print(zero["Year"].value_counts().sort_index().tail(6))