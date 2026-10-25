import pandas as pd

df = pd.read_csv("data/contracts.csv", low_memory=False)
print("raw:", len(df))

# look at what raw amounts look like
print(df["Award Amount"].head(15))

df["Award Amount"] = df["Award Amount"].astype(str)
df["Award Amount"] = df["Award Amount"].str.replace("$", "", regex=False)
df["Award Amount"] = df["Award Amount"].str.replace(",", "", regex=False)
df["Award Amount"] = pd.to_numeric(df["Award Amount"], errors="coerce")
print("blank amounts after converting:", df["Award Amount"].isna().sum())

df["Approval Date"] = pd.to_datetime(df["Approval Date"], errors="coerce")
df["Year"] = df["Approval Date"].dt.year

df = df[df["Year"] >= 2023]
df = df[df["Year"] <= 2025]
print("2023-2025:", len(df))

df = df[df["Award Amount"].notna()]
print("amount not blank:", len(df))

df = df[df["Award Amount"] != 0]
print("amount not zero:", len(df))

print("blank contract ids:", df["Purchase Order (Contract) Number"].isna().sum())
print("unique contract ids:", df["Purchase Order (Contract) Number"].nunique())
print("positive rows:", (df["Award Amount"] > 0).sum())
print("negative rows:", (df["Award Amount"] < 0).sum())

contracts = df.groupby("Purchase Order (Contract) Number").agg({"Award Amount": "sum"})
print("contracts after rollup:", len(contracts))

contracts = contracts[contracts["Award Amount"] > 0]
print("contracts with positive total:", len(contracts))
print("total spend:", contracts["Award Amount"].sum())

clean = pd.read_csv("output/contracts_clean.csv")
print("rows in clean csv:", len(clean))
print("clean csv total spend:", clean["Award Amount"].sum())