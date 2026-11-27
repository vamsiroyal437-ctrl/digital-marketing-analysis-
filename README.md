# Digital Marketing Campaign Analysis

A beginner-friendly portfolio project that analyzes sample marketing campaign performance across Instagram, Google Ads, Facebook, Email and YouTube.

## Objective
Compare campaign performance and understand how advertising spend relates to clicks, conversions and revenue.

## Tools
- Python
- Pandas
- CSV datasets

## KPIs
- **CTR (Click-through rate):** clicks ÷ impressions × 100
- **Conversion rate:** conversions ÷ clicks × 100
- **CPC (Cost per click):** spend ÷ clicks
- **CPA (Cost per acquisition):** spend ÷ conversions
- **ROAS (Return on ad spend):** revenue ÷ spend

## Project files
- `data/campaign_data.csv` — sample campaign data
- `analyze_campaigns.py` — calculates KPIs and exports a report
- `reports/campaign_analysis.csv` — generated KPI output (run the script to refresh)

## Run it
```bash
pip install -r requirements.txt
python analyze_campaigns.py
```

## Sample-data disclaimer
The dataset is synthetic and created for practice. It is not actual client or platform data.

## Portfolio improvements
1. Visualize channel KPIs in Power BI or Excel.
2. Add budget recommendations based on ROAS and CPA.
3. Replace the sample data with anonymized real campaign data if available.
