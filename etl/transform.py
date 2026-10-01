import pandas as pd


def transform_data(data):
    """
    Transform raw cryptocurrency data received from CoinMarketCap API.
    """

    transformed_records = []

    for coin in data:
        # Get the USD market data from the API response
        usd_data = coin["quote"][0]

        record = {
            "name": coin["name"],
            "symbol": coin["symbol"],
            "rank": coin["cmc_rank"],
            "price_usd": usd_data["price"],
            "market_cap": usd_data["market_cap"],
            "volume_24h": usd_data["volume_24h"],
            "percent_change_24h": usd_data["percent_change_24h"]
        }

        transformed_records.append(record)

    # Convert the list of records into a DataFrame
    transformed_df = pd.DataFrame(transformed_records)

    print("\nData after extracting required fields:")
    print(transformed_df)

    # Convert numeric columns
    numeric_columns = [
        "rank",
        "price_usd",
        "market_cap",
        "volume_24h",
        "percent_change_24h"
    ]

    for column in numeric_columns:
        transformed_df[column] = pd.to_numeric(
            transformed_df[column],
            errors="coerce"
        )

    # Remove rows containing required missing values
    transformed_df = transformed_df.dropna(
        subset=[
            "name",
            "symbol",
            "rank",
            "price_usd",
            "market_cap"
        ]
    )

    # Keep only valid positive values
    transformed_df = transformed_df[
        (transformed_df["rank"] > 0)
        & (transformed_df["price_usd"] > 0)
        & (transformed_df["market_cap"] > 0)
    ]

    # Convert market cap into billions
    transformed_df["market_cap_billion"] = (
        transformed_df["market_cap"] / 1_000_000_000
    )

    return transformed_df


if __name__ == "__main__":
    from etl.extract import extract_data

    # Extract real data from CoinMarketCap
    data = extract_data(limit=3)

    # Transform the API data
    transformed_data = transform_data(data)

    print("\nTransformation completed successfully.")
    print("\nFinal transformed data:")
    print(transformed_data)