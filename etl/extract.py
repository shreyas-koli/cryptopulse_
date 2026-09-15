import pandas as pd


def extract_data():
    df = pd.read_csv("data/raw/sample_crypto.csv")
    return df



data = extract_data()    
print(data)