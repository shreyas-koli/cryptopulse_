import pandas as pd


def transform_data(df):
    print("Available columns before cleaning:")
    print(df.columns.tolist())

    # Create a copy of the original DataFrame
    transformed_df = df.copy()

    # Remove extra spaces from column names
    transformed_df.columns = transformed_df.columns.str.strip()

    print("Available columns after cleaning:")
    print(transformed_df.columns.tolist())

    # Convert price and market cap into numeric values
    transformed_df["price_usd"] = pd.to_numeric(
        transformed_df["price_usd"],
        errors="coerce"
    )

    transformed_df["market_cap"] = pd.to_numeric(
        transformed_df["market_cap"],
        errors="coerce"
    )

    # Remove rows containing missing values
    transformed_df = transformed_df.dropna(
        subset=["name", "symbol", "price_usd", "market_cap"]
    )

    transformed_df = transformed_df[
        (transformed_df["price_usd"] > 0)
        & (transformed_df["market_cap"] > 0)
    ]

    transformed_df["market_cap_billion"] = (
        transformed_df["market_cap"]/1_000_000_000
    )

    return transformed_df


if __name__ == "__main__":
    df = pd.read_csv("data/raw/sample_crypto.csv")

    transformed_data = transform_data(df)

    transformed_data.to_csv(
        "data/processed/transformed_crypto.csv",
        index=False
    )


    print("Transformation completed successfully.")
    print("Saved file: data/processed/transformed_crypto.csv")
    print(transformed_data)