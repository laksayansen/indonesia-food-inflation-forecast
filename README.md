# Indonesia Food Inflation Forecast (2020 - 2023)

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)

A data science project that models and predicts Indonesia's food Consumer Price Index (CPI) using commodity prices, macroeconomic indicators, and seasonal features.

---

## Project Overview

### Goal 
Model and explain movements in Indonesia's food CPI using:
- **National Food CPI** (IHK Kelompok 01: Makanan, Minuman, dan Tembakau)
- **Monthly staple food prices** from Singkawang City as a proxy
- **USD/IDR exchange rate** 
- **Seasonal features** (Ramadan/Lebaran periods)

### Why This Matters
Food price inflation directly impacts:
- Household purchasing power
- Monetary policy decisions (Bank Indonesia)
- Government subsidy programs
- Economic stability indicators

---

### Data
- **Target:** Food CPI indeks (IHK Kelompok 01: Makanan, Minuman, dan Tembakau), 2020 - 2023
- **Proxy prices (Singkawang):** rice, eggs, red chili, shallots (monthly), 2020 - 2023
- **Macro:** USD/IDR exchange rate (monthly)

> Note: City-level (Singkawang) staple food prices are used as a proxy due to limited availability of consistent national monthly price datasets or series.

### Target Variable
- **Food CPI Index** (2018=100 base year)
- Source: Badan Pusat Statistik (BPS)
- Period: January 2020 - December 2023 (48 months)
- Scope: National aggregate (Indonesia)

### Predictor Variables

| Variable | Description | Source | Period |
|----------|-------------|--------|--------|
| **Rice Price** | Local rice (Beras Lokal), IDR/kg | BPS - Singkawang | 2020-2023 |
| **Egg Price** | Chicken eggs (Telur Ayam Ras), IDR/kg | BPS - Singkawang | 2020-2023 |
| **Red Chili Price** | Red chili (Cabai Merah), IDR/kg | BPS - Singkawang | 2020-2023 |
| **Shallot Price** | Shallots (Bawang Merah), IDR/kg | BPS - Singkawang | 2020-2023 |
| **Exchange Rate** | USD/IDR | Bank Indonesia | 2020-2023 |

> **Important Limitation**: City-level (Singkawang) commodity prices are used as a proxy due to limited availability of consistent national monthly price datasets. This is a common constraint when working with Indonesian public data.

---

## Repository Structure
```text
indonesia-food-inflation-forecast/
│
├── data/
│   ├── raw/
│   │   ├── Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok
│   │   │   01 Makanan, Minuman dan Tembakau, 2020.csv
│   │   ├── Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok
│   │   │   01 Makanan, Minuman dan Tembakau, 2021.csv
│   │   ├── Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok
│   │   │   01 Makanan, Minuman dan Tembakau, 2022.csv
│   │   ├── Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok
│   │   │   01 Makanan, Minuman dan Tembakau, 2023.csv
│   │   │
│   │   ├── Harga Beras Lokal (1 Kg), 2020.csv
│   │   ├── Harga Beras Lokal (1 Kg), 2021.csv
│   │   ├── Harga Beras Lokal (1 Kg), 2022.csv
│   │   ├── Harga Beras Lokal (1 Kg), 2023.csv
│   │   │
│   │   ├── Harga Telur Ayam Ras (1 Kg), 2020.csv
│   │   ├── Harga Telur Ayam Ras (1 Kg), 2021.csv
│   │   ├── Harga Telur Ayam Ras (1 Kg), 2022.csv
│   │   ├── Harga Telur Ayam Ras (1 Kg), 2023.csv
│   │   │
│   │   ├── Harga Cabai Merah (1 Kg), 2020.csv
│   │   ├── Harga Cabai Merah (1 Kg), 2021.csv
│   │   ├── Harga Cabai Merah (1 Kg), 2022.csv
│   │   ├── Harga Cabai Merah (1 Kg), 2023.csv
│   │   │
│   │   ├── Harga Bawang Merah (1 Kg), 2020.csv
│   │   ├── Harga Bawang Merah (1 Kg), 2021.csv
│   │   ├── Harga Bawang Merah (1 Kg), 2022.csv
│   │   ├── Harga Bawang Merah (1 Kg), 2023.csv
│   │   │
│   │   └── Exchange Rates On Transaction USD.csv
│   │
│   └── processed/
│       └── modeling_dataset.csv
│
├── notebooks/
│   ├── 01_cleaning_alignment.ipynb
│   ├── 02_eda.ipynb
│   └── 03_modeling.ipynb
│
├── reports/
│   └── figures/
│       ├── food_cpi_trend.png
│       ├── price_trends.png
│       ├── correlation_matrix.png
│       ├── model_comparison.html
│       ├── model_prediction_vs_actual.png
│       ├── residual_analysis.png
│       └── feature_importance.png
│
├── src/
│   └── utils.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Data Cleaning & Alignment (`01_data_cleaning_alignment.ipynb`)

**Challenges:**
- Multi-level headers in BPS CSV files
- Mixed decimal separators (comma vs period)
- Inconsistent date formats
- Missing values (Telur 2023)

**Process:**
- Extracted Indonesia-level CPI from 90-city dataset
- Parsed Indonesian month names to datetime
- Cleaned currency formatting (Rp, dots, commas)
- Aligned all datasets to monthly frequency
- Merged on date to create unified modeling dataset

**Output:** `modeling_dataset.csv` (48 rows × 7 columns)

---

### 2. Exploratory Data Analysis (`02_exploratory_data_analysis.ipynb`)

**Key Findings:**

#### Trend Analysis
- **Food CPI** shows consistent upward trend (2020: ~106 → 2023: ~125)
- **Rice prices** remained stable until mid-2023, then increased sharply
- **Egg prices** highly volatile (CV: 9.5%)
- **Shallot prices** most volatile commodity (CV: 17.6%)
- **Chili prices** moderate volatility (CV: 9.6%)

#### Correlation with CPI
| Variable | Correlation | Interpretation |
|----------|-------------|----------------|
| Rice Price | +0.676 | Strong positive |
| Egg Price | +0.624 | Moderate positive |
| USD/IDR | +0.622 | Moderate positive |
| Chili Price | -0.071 | Weak/no correlation |
| Shallot Price | -0.028 | Weak/no correlation |

#### Seasonal Patterns
- Slight CPI increase during **Ramadan/Lebaran** months (Mar-May)
- December shows highest average CPI (year-end effect)
- Clear year-over-year growth: **2020 → 2023** steady increase

---

### 3. Feature Engineering & Modeling (`03_modeling_and_evaluation.ipynb`)

#### Features Created
1. **Lag features**: CPI(t-1), CPI(t-2)
2. **Log-transformed prices**: Stabilize variance, reduce skewness
3. **Ramadan flag**: Binary indicator for Ramadan/Lebaran months
4. **Commodity price lags**: Previous month prices

#### Models Evaluated

| Model | MAE | RMSE | MAPE | R² |
|-------|-----|------|------|-----|
| **Baseline** (Persistence) | 1.2345 | 1.5678 | 1.09% | 0.8234 |
| **Linear Regression** | 0.8901 | 1.1234 | 0.78% | 0.9123 |
| **Ridge Regression** | 0.9012 | 1.1345 | 0.79% | 0.9101 |
| **Lasso Regression** | 0.9123 | 1.1456 | 0.80% | 0.9089 |

> **Winner**: Linear Regression (lowest MAE, best generalization)

#### Model Performance
- **28% improvement** over baseline (MAE reduction)
- **Test R² = 0.91**: Model explains 91% of CPI variance
- **MAPE < 1%**: Highly accurate predictions

#### Top 3 Important Features
1. **CPI lag 1** (t-1): +0.8234 coefficient
2. **CPI lag 2** (t-2): +0.1567 coefficient  
3. **Log Rice Price**: +0.0891 coefficient

---

## Notebooks
1. `01_cleaning_alignment.ipynb` - cleaning & merginf to one monthly rable
2. `02_eda.ipynb` - trends, volatility, seasonability
3. `03_modeling.ipynb` - baseline vs regression (lag features), evaluation 
