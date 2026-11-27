"""Analyze a small digital marketing campaign dataset."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "campaign_data.csv"
OUT = ROOT / "reports" / "campaign_analysis.csv"

df = pd.read_csv(DATA)
df["CTR_%"] = (df["Clicks"] / df["Impressions"] * 100).round(2)
df["Conversion_Rate_%"] = (df["Conversions"] / df["Clicks"] * 100).round(2)
df["CPC"] = (df["Spend"] / df["Clicks"]).round(2)
df["CPA"] = (df["Spend"] / df["Conversions"]).round(2)
df["ROAS"] = (df["Revenue"] / df["Spend"]).round(2)
df.to_csv(OUT, index=False)

print("Campaign KPI report saved to", OUT)
print(df[["Campaign", "Channel", "CTR_%", "Conversion_Rate_%", "CPC", "CPA", "ROAS"]].to_string(index=False))
print("\nOverall spend: ₹", int(df["Spend"].sum()))
print("Overall revenue: ₹", int(df["Revenue"].sum()))
print("Overall ROAS: ", round(df["Revenue"].sum() / df["Spend"].sum(), 2))
