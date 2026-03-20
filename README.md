# 📊 Romania Macroeconomic EDA (2000–2024)

An exploratory data analysis (EDA) of Romania's key macroeconomic indicators over a 24-year period, built with Python. This project applies statistical methods and data visualization techniques to identify economic trends, cycles, and structural patterns in the Romanian economy.

> **Data sources:** National Institute of Statistics (INS – TEMPO), Eurostat, National Bank of Romania (BNR)

---

## 🔍 What This Project Covers

- **GDP growth** — nominal evolution and annual growth rates (2000–2024)
- **Inflation** — yearly CPI trends with critical threshold analysis
- **Unemployment** — cyclical patterns across economic shocks (2009 crisis, COVID-19)
- **Trade balance** — export vs. import dynamics and persistent trade deficit
- **Exchange rate** — EUR/RON evolution over time
- **Wages** — nominal vs. real salary comparison (purchasing power analysis)
- **Phillips Curve** — relationship between inflation and unemployment
- **Correlation matrix** — Pearson correlations between all macroeconomic variables

---

## 📁 Project Structure

```
romania-macro-eda/
│
├── romania_macro_eda.py          # Main Python script
├── romania_macro_2000_2024.csv   # Processed dataset with derived indicators
│
├── fig1_dashboard_macro.png      # Main dashboard (6 indicators)
├── fig2_corelatii_distributii.png # Correlation heatmap + distributions
└── fig3_cicluri_economice.png    # Economic cycles & derived analysis
```

---

## 📈 Key Findings

| Indicator | Value |
|-----------|-------|
| GDP growth (2000–2024) | ~8x increase |
| Median inflation | 5.9% |
| Peak inflation | 45.7% (2000) |
| Minimum unemployment | 4.3% (2018) |
| Avg. trade deficit | -5.6 bn EUR/year |
| Real wage growth (2000–2024) | +43% |
| GDP–Salary correlation | 0.993 |

---

## 🛠️ Tech Stack

| Library | Usage |
|---------|-------|
|  | Data manipulation and aggregation |
|  | Numerical computations |
|  | Core visualizations and dashboards |
|  | Correlation heatmap and styled plots |
|  | Statistical analysis (Pearson, linear regression) |

---

## 👤 Author

**Alexandru Georgian Neculae**  
Statistics & Data Science Student — Bucharest Academy of Economic Studies  
Data Analysis Practic Student — National Institute of Statistics (INS Romania)  
