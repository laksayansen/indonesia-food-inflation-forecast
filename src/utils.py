"""
Utility functions for the Indonesian Food Inflation Forecast project
"""
import pandas as pd
import numpy as np

def clean_currency_string(value):
    """Clean Indonesian currency format to numeric
    
    Example:
        'Rp 12.500,00' --> 12500.0
        '12.500' --> 12500.0
        '12.500,00' --> 12500.0
    """
    if pd.isna(value):
        return np.nan
    value = str(value)
    value = value.replace('Rp', '').replace(" ", '').strip()
    value = value.replace('.', '')
    value = value.replace(',', '.')

    try:
        return float(value)
    except:
        return np.nan

    
def extract_month_from_column(month_name):
    """
    Extract month number from Indonesian month name in colun

    Example:
        'Januari' --> 1
        'Februari' --> 2
    """
    month_map = {
        'januari': 1, 'februari': 2, 'maret': 3, 'april': 4, 'mei': 5,
        'juni': 6, 'juli': 7, 'agustus': 8, 'september': 9,
        'oktober': 10, 'november': 11, 'desember': 12
    }
    if pd.isna(month_name):
        return None
    
    month_lower = str(month_name).lower().strip()

    for month_name_key, month_num in month_map.items():
        if month_name_key in month_lower:
            return month_num
        
    return None


def add_ramadan_flag(df, date_col='date'):
    """
    Add binary flag for Ramadan/Eid months.

    Ramadan periods (approximate):
    - 2020: April-May
    - 2021: April-May
    - 2022: April-May
    - 2023: March-April
    """
    df = df.copy()
    df['is_ramadan'] = 0
    ramadan_periods = [
        ('2020-04', '2020-05'),
        ('2021-04', '2021-05'),
        ('2022-04', '2022-05'),
        ('2023-03', '2023-04')
    ]

    df['year_month'] = df[date_col].dt.to_period('M').astype(str)

    for start_momth, end_month in ramadan_periods:
        mask = df['year_month'].isin([start_momth, end_month])
        df.loc[mask, 'is_ramadan'] = 1
    
    df = df.drop(columns=['year_month'])

    return df
    

def create_lag_features(df, value_col, lags=[1, 2], date_col='date'):
    """
    Create lagged features for time series data.

    Args:
        df: Input dataframe (must be sorted by date)
        value_col: Column to create lags from
        lags: List of lag periods
        date_col: Date column name

    Returns:
        Dataframe with additional lag columns
    """
    df = df.sort_values(date_col).copy()

    for lag in lags:
        df[f'{value_col}_lag{lag}'] = df[value_col].shift(lag)

    return df

def calculate_metrics(y_true, y_pred):
    """
    Calculate regression metrics: MAE, RMSE, MAPE, R²
    """
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mask = y_true != 0

    if mask.sum() > 0:
        mape = np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
    else:
        mape = np.nan
    
    r2 = r2_score(y_true, y_pred)
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape,
        'R²': r2
    }
