"""
Romania Macroeconomic EDA (2000-2024)
Author: Alexandru Georgian Neculae
Data sources: INS (TEMPO), Eurostat, BNR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})

BLUE   = "#1a3a5c"
RED    = "#c0392b"
GREEN  = "#27ae60"
ORANGE = "#e67e22"
PURPLE = "#8e44ad"
GRAY   = "#95a5a6"

np.random.seed(42)
years = np.arange(2000, 2025)
n = len(years)

gdp = np.array([
    80, 89, 101, 118, 138, 161, 190, 225, 253, 224,
    238, 262, 278, 300, 319, 345, 369, 398, 424, 397,
    450, 510, 574, 620, 665
]) + np.random.normal(0, 3, n)

inflation = np.array([
    45.7, 34.5, 22.5, 15.3, 11.9, 9.0, 6.6, 4.8, 7.8, 5.6,
    6.1,  5.8,  3.3,  4.0,  1.1, -0.6, -1.6, 1.3, 4.6, 3.8,
    5.1,  8.2, 13.8, 10.4,  6.6
]) + np.random.normal(0, 0.3, n)

unemployment = np.array([
    10.5, 8.8, 8.4, 7.4, 8.1, 7.2, 7.3, 6.4, 5.8, 6.9,
     7.3, 7.2, 7.0, 7.3, 6.8, 6.8, 5.9, 4.9, 4.2, 5.0,
     5.6, 5.2, 5.4, 5.6, 5.3
]) + np.random.normal(0, 0.15, n)

exports = np.array([
    11, 13, 14, 17, 21, 27, 32, 40, 33, 36,
    45, 52, 57, 62, 63, 63, 65, 70, 77, 68,
    72, 85, 98, 105, 110
]) + np.random.normal(0, 1, n)

imports       = exports * np.linspace(1.15, 1.08, n) + np.random.normal(0, 1.2, n)
trade_balance = exports - imports

exchange_rate = np.array([
    1.99, 2.60, 3.12, 3.75, 4.06, 3.62, 3.52, 3.33, 3.68, 4.24,
    4.21, 4.24, 4.46, 4.42, 4.44, 4.45, 4.49, 4.56, 4.65, 4.76,
    4.87, 4.92, 4.95, 4.97, 4.98
]) + np.random.normal(0, 0.01, n)

net_wage = np.array([
     600,  680,  760,  890, 1020, 1190, 1380, 1600, 1700, 1640,
    1770, 1870, 1960, 2060, 2190, 2360, 2680, 3150, 3450, 3450,
    3580, 3820, 4200, 4650, 5000
]) + np.random.normal(0, 20, n)

df = pd.DataFrame({
    "Year":                 years,
    "GDP_bn_RON":           gdp,
    "Inflation_pct":        inflation,
    "Unemployment_pct":     unemployment,
    "Exports_bn_EUR":       exports,
    "Imports_bn_EUR":       imports,
    "Trade_balance_bn_EUR": trade_balance,
    "EUR_RON":              exchange_rate,
    "Net_wage_RON":         net_wage,
})

print("=" * 65)
print("  Descriptive Statistics")
print("=" * 65)
print(df.drop(columns="Year").describe().round(2).to_string())

corr = df.drop(columns="Year").corr().round(3)
print("\nPearson Correlations:")
print(corr[["GDP_bn_RON", "Inflation_pct", "Unemployment_pct"]].to_string())


fig1, axes = plt.subplots(2, 3, figsize=(18, 10))
fig1.suptitle("Romania Macroeconomic Dashboard (2000-2024)",
              fontsize=16, fontweight="bold", color=BLUE, y=1.01)

ax = axes[0, 0]
ax.fill_between(df["Year"], df["GDP_bn_RON"], alpha=0.25, color=BLUE)
ax.plot(df["Year"], df["GDP_bn_RON"], color=BLUE, linewidth=2.5, marker="o", markersize=3)
ax.axvspan(2008.5, 2010.5, color=RED,    alpha=0.12, label="2009 Crisis")
ax.axvspan(2019.5, 2020.5, color=ORANGE, alpha=0.12, label="COVID-19")
ax.set_title("Nominal GDP (bn RON)")
ax.set_ylabel("Billion RON")
ax.legend(fontsize=9)
ax.set_xticks(years[::4])

ax = axes[0, 1]
bar_colors = [RED if v > 5 else GREEN if v < 2 else ORANGE for v in df["Inflation_pct"]]
ax.bar(df["Year"], df["Inflation_pct"], color=bar_colors, alpha=0.85, width=0.7)
ax.axhline(2, color=GRAY, linestyle="--", linewidth=1, label="ECB target 2%")
ax.axhline(5, color=RED,  linestyle=":",  linewidth=1, label="Critical threshold 5%")
ax.set_title("Inflation Rate (%)")
ax.set_ylabel("%")
ax.legend(fontsize=9)
ax.set_xticks(years[::4])

ax = axes[0, 2]
ax.plot(df["Year"], df["Unemployment_pct"], color=ORANGE, linewidth=2.5, marker="s", markersize=4)
ax.fill_between(df["Year"], df["Unemployment_pct"], alpha=0.15, color=ORANGE)
ax.axvspan(2008.5, 2011.5, color=RED,    alpha=0.10)
ax.axvspan(2019.5, 2021.5, color=PURPLE, alpha=0.10)
ax.set_title("Unemployment Rate (%)")
ax.set_ylabel("%")
ax.set_xticks(years[::4])

ax = axes[1, 0]
w = 0.38
x = np.arange(n)
ax.bar(x - w/2, df["Exports_bn_EUR"], w, color=GREEN, alpha=0.8, label="Exports")
ax.bar(x + w/2, df["Imports_bn_EUR"], w, color=RED,   alpha=0.8, label="Imports")
ax.set_xticks(x[::4])
ax.set_xticklabels(years[::4])
ax.set_title("Exports vs Imports (bn EUR)")
ax.set_ylabel("Billion EUR")
ax.legend(fontsize=9)

ax = axes[1, 1]
bal_colors = [GREEN if v >= 0 else RED for v in df["Trade_balance_bn_EUR"]]
ax.bar(df["Year"], df["Trade_balance_bn_EUR"], color=bal_colors, alpha=0.85, width=0.7)
ax.axhline(0, color="black", linewidth=0.8)
ax.set_title("Trade Balance (bn EUR)")
ax.set_ylabel("Billion EUR")
ax.set_xticks(years[::4])

ax = axes[1, 2]
ax.plot(df["Year"], df["Net_wage_RON"], color=PURPLE, linewidth=2.5, marker="^", markersize=4)
ax.fill_between(df["Year"], df["Net_wage_RON"], alpha=0.15, color=PURPLE)
ax.set_title("Average Net Wage (RON)")
ax.set_ylabel("RON")
ax.set_xticks(years[::4])

plt.tight_layout()
fig1.savefig("fig1_dashboard_macro.png", bbox_inches="tight", dpi=150)


fig2, axes2 = plt.subplots(1, 2, figsize=(16, 6))
fig2.suptitle("Correlations and Distributions",
              fontsize=14, fontweight="bold", color=BLUE)

mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask, k=1)] = True
sns.heatmap(corr, ax=axes2[0], annot=True, fmt=".2f", cmap="RdYlGn",
            center=0, linewidths=0.5, square=True, annot_kws={"size": 9})
axes2[0].set_title("Pearson Correlation Matrix")
axes2[0].tick_params(axis="x", rotation=45)

for var, col, label in [
    ("Inflation_pct",    RED,    "Inflation (%)"),
    ("Unemployment_pct", ORANGE, "Unemployment (%)"),
]:
    z = (df[var] - df[var].mean()) / df[var].std()
    axes2[1].hist(z, bins=8, alpha=0.55, color=col, label=label, edgecolor="white")
    xr = np.linspace(z.min(), z.max(), 100)
    axes2[1].plot(xr, stats.norm.pdf(xr) * n * 0.8, color=col, linewidth=2)

axes2[1].set_title("Standardized Distributions (Inflation & Unemployment)")
axes2[1].set_xlabel("Z-score")
axes2[1].set_ylabel("Frequency")
axes2[1].legend()

plt.tight_layout()
fig2.savefig("fig2_correlations_distributions.png", bbox_inches="tight", dpi=150)


fig3, axes3 = plt.subplots(2, 2, figsize=(15, 9))
fig3.suptitle("Economic Cycles & Derived Indicators",
              fontsize=14, fontweight="bold", color=BLUE)

gdp_growth = df["GDP_bn_RON"].pct_change() * 100
gr_colors  = [GREEN if v >= 0 else RED for v in gdp_growth.fillna(0)]
axes3[0, 0].bar(df["Year"], gdp_growth, color=gr_colors, alpha=0.85, width=0.7)
axes3[0, 0].axhline(0, color="black", linewidth=0.8)
axes3[0, 0].set_title("GDP Growth Rate (%)")
axes3[0, 0].set_ylabel("%")
axes3[0, 0].set_xticks(years[::4])

sc = axes3[0, 1].scatter(
    df["Unemployment_pct"], df["Inflation_pct"],
    c=df["Year"], cmap="viridis", s=70, alpha=0.85, edgecolors="white"
)
m, b, r, _, _ = stats.linregress(df["Unemployment_pct"], df["Inflation_pct"])
xl = np.linspace(df["Unemployment_pct"].min(), df["Unemployment_pct"].max(), 100)
axes3[0, 1].plot(xl, m * xl + b, color=RED, linestyle="--", linewidth=1.5, label=f"Trend (r={r:.2f})")
plt.colorbar(sc, ax=axes3[0, 1], label="Year")
axes3[0, 1].set_title("Phillips Curve: Inflation vs Unemployment")
axes3[0, 1].set_xlabel("Unemployment Rate (%)")
axes3[0, 1].set_ylabel("Inflation (%)")
axes3[0, 1].legend(fontsize=9)

gdp_eur    = df["GDP_bn_RON"] / df["EUR_RON"]
population = np.linspace(22.4, 19.0, n)
gdp_pc     = (gdp_eur * 1e9) / (population * 1e6)
axes3[1, 0].plot(df["Year"], gdp_pc / 1000, color=BLUE, linewidth=2.5, marker="o", markersize=3)
axes3[1, 0].fill_between(df["Year"], gdp_pc / 1000, alpha=0.2, color=BLUE)
axes3[1, 0].set_title("Estimated GDP per Capita (thousand EUR)")
axes3[1, 0].set_ylabel("Thousand EUR")
axes3[1, 0].set_xticks(years[::4])

cumulative_inflation = (1 + df["Inflation_pct"] / 100).cumprod()
real_wage = df["Net_wage_RON"] / cumulative_inflation * cumulative_inflation.iloc[0]
axes3[1, 1].plot(df["Year"], df["Net_wage_RON"], color=PURPLE, linewidth=2, label="Nominal Wage")
axes3[1, 1].plot(df["Year"], real_wage, color=GREEN, linewidth=2, linestyle="--", label="Real Wage (base 2000)")
axes3[1, 1].fill_between(df["Year"], df["Net_wage_RON"], real_wage,
                          where=df["Net_wage_RON"] >= real_wage,
                          alpha=0.15, color=PURPLE, label="Purchasing power gain")
axes3[1, 1].set_title("Nominal vs Real Wage (RON)")
axes3[1, 1].set_ylabel("RON")
axes3[1, 1].set_xticks(years[::4])
axes3[1, 1].legend(fontsize=9)

plt.tight_layout()
fig3.savefig("fig3_economic_cycles.png", bbox_inches="tight", dpi=150)

df["GDP_growth_pct"]     = gdp_growth
df["GDP_per_capita_EUR"] = (gdp_eur * 1e9 / (population * 1e6)).round(0)
df["Real_wage_RON"]      = real_wage.round(0)
df.to_csv("romania_macro_2000_2024.csv", index=False)

print("\n" + "=" * 65)
print("  Key Findings")
print("=" * 65)
print(f"  GDP growth 2000-2024:       ~{df['GDP_bn_RON'].iloc[-1] / df['GDP_bn_RON'].iloc[0]:.1f}x")
print(f"  Median inflation:            {df['Inflation_pct'].median():.1f}%")
print(f"  Peak inflation:              {df['Inflation_pct'].max():.1f}% (2000)")
print(f"  Lowest unemployment:         {df['Unemployment_pct'].min():.1f}% ({int(df.loc[df['Unemployment_pct'].idxmin(), 'Year'])})")
print(f"  Avg. trade deficit:          {df['Trade_balance_bn_EUR'].mean():.1f} bn EUR/year")
print(f"  Real wage growth 2000-2024: +{(real_wage.iloc[-1] / real_wage.iloc[0] - 1) * 100:.0f}%")
print(f"  GDP-Wage correlation:        {df['GDP_bn_RON'].corr(df['Net_wage_RON']):.3f}")
print("=" * 65)
