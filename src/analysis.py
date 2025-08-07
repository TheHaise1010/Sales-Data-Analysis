# src/analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_by_month(df: pd.DataFrame):
    monthly_sales = df.groupby('Month')['Sales'].sum()
    monthly_sales.plot(kind='bar', title='Total Sales per Month')
    plt.xlabel('Month')
    plt.ylabel('Sales ($)')
    plt.tight_layout()
    plt.show()

def plot_top_products(df: pd.DataFrame):
    top_products = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(10)
    top_products.plot(kind='barh', title='Top 10 Products Sold')
    plt.xlabel('Quantity')
    plt.ylabel('Product')
    plt.tight_layout()
    plt.show()

def plot_sales_by_city(df: pd.DataFrame):
    sales_by_city = df.groupby('City')['Sales'].sum()
    sales_by_city.plot(kind='bar', title='Sales by City')
    plt.ylabel('Sales ($)')
    plt.tight_layout()
    plt.show()

def plot_hourly_sales(df: pd.DataFrame):
    hourly_orders = df.groupby('Hour')['Order ID'].count()
    sns.lineplot(x=hourly_orders.index, y=hourly_orders.values)
    plt.title('Orders by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Number of Orders')
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.show()
