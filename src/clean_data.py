import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    # Elimina filas nulas
    df = df.dropna()

    # Convierte "Order Date" a datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y %H:%M:%S')

    # Crea una columna de ingresos: Quantity * Price
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']

    # Extrae mes y hora para análisis
    df['Month'] = df['Order Date'].dt.month
    df['Hour'] = df['Order Date'].dt.hour
    df['City'] = df['Purchase Address'].apply(lambda x: x.split(",")[1].strip())

    return df
