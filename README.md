<<<<<<< HEAD
# Indonesia Food Inflation Forecast (2020 - 2023)

## Goal 
Model and explain movements in Indonesia's food CPI using:
- National Food CPI index 
- Monthly staple food prices (Singkawang City) as a proxy
- USD/IDR exchange rate
- Seasonality featurers (month, Ramadan and Eid)

## Data
- **Target:** Food CPI indeks (IHK Kelompok 01: Makanan, Minuman, dan Tembakau), 2020 - 2023
- **Proxy prices (Singkawang):** rice, eggs, red chili, shallots (monthly), 2020 - 2023
- **Macro:** USD/IDR exchange rate (monthly)

> Note: City-level (Singkawang) staple food prices are used as a proxy due to limited availability of consistent national monthly price datasets or series.

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
│   ├── 01_data_cleaning_alignment.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   └── 03_modeling_and_evaluation.ipynb
│
├── reports/
│   └── figures/
│       ├── food_cpi_trend.png
│       ├── price_trends.png
│       └── model_prediction_vs_actual.png
│
├── src/
│   └── utils.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Notebooks
1. `01_cleaning_alignment.ipynb` - cleaning & merginf to one monthly rable
2. `02_eda.ipynb` - trends, volatility, seasonability
3. `03_modeling.ipynb` - baseline vs regression (lag features), evaluation 
