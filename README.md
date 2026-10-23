# Romania Macroeconomic EDA (2000-2024)

An exploratory data analysis in Python that practices common macroeconomic analysis techniques on an illustrative dataset of Romania-like indicators.

> **Note on data:** the dataset in this repository is illustrative. Values are approximate, entered manually and perturbed with random noise. They are not official statistics from INS, Eurostat or BNR, and the results should not be read as findings about the real Romanian economy. The goal of the project is the analysis workflow.

## What the project covers

- GDP: nominal evolution and annual growth rates
- Inflation: yearly trends with threshold markers
- Unemployment: patterns around the 2009 crisis and COVID-19
- Trade balance: exports vs. imports
- Exchange rate: EUR/RON
- Wages: nominal vs. real wage
- Phillips curve: inflation vs. unemployment
- Pearson correlation matrix across all variables

## Project structure

romania-macro-eda/
├── romania_macro_eda.py            # Main script
├── romania_macro_2000_2024.csv     # Illustrative dataset with derived indicators
├── fig1_dashboard_macro.png
├── fig2_corelatii_distributii.png
└── fig3_cicluri_economice.png

## Tech stack

Python, pandas, NumPy, matplotlib, seaborn, SciPy

## Author

Alexandru Georgian Neculae
Statistics and Economic Forecasting student, Bucharest Academy of Economic Studies (ASE)
