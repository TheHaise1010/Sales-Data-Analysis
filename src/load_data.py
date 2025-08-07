import pandas as pd

def load_sales_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)
    return df
