# main.py

from src.load_data import load_sales_data
from src.clean_data import clean_sales_data
from src.analysis import (
    plot_sales_by_month,
    plot_top_products,
    plot_sales_by_city,
    plot_hourly_sales
)

if __name__ == '__main__':
    path = 'data/sales.csv'
    df_raw = load_sales_data(path)
    df_clean = clean_sales_data(df_raw)

    plot_sales_by_month(df_clean)
    plot_top_products(df_clean)
    plot_sales_by_city(df_clean)
    plot_hourly_sales(df_clean)
