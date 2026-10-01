import pandas as pd
from pathlib import Path

from database.connection import get_connection


SCHEMA_FILE = "database/schema.sql"


def create_table():
    """
    Create the crypto_market_data table if it does not exist.
    """

    schema_path = Path(SCHEMA_FILE)
    schema_sql = schema_path.read_text()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(schema_sql)
        connection.commit()

        print("Table created successfully.")

        cursor.close()

    finally:
        connection.close()

        print("Database connection closed.")

def load_data(df):
    """
    Insert new cryptocurrencies, update existing ones,
    and remove cryptocurrencies that are no longer
    part of the current API snapshot.
    """

    if df.empty:
        print("No data available. Skipping database update.")
        return

    connection = get_connection()

    try:
        cursor = connection.cursor()

        upsert_query = """
            INSERT INTO crypto_market_data (
                name,
                symbol,
                rank,
                price_usd,
                market_cap,
                volume_24h,
                percent_change_24h,
                market_cap_billion
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

            ON CONFLICT (symbol)
            DO UPDATE SET
                name = EXCLUDED.name,
                rank = EXCLUDED.rank,
                price_usd = EXCLUDED.price_usd,
                market_cap = EXCLUDED.market_cap,
                volume_24h = EXCLUDED.volume_24h,
                percent_change_24h = EXCLUDED.percent_change_24h,
                market_cap_billion = EXCLUDED.market_cap_billion,
                loaded_at = CURRENT_TIMESTAMP
        """

        # Insert or update current API records
        for _, row in df.iterrows():
            cursor.execute(
                upsert_query,
                (
                    row["name"],
                    row["symbol"],
                    row["rank"],
                    row["price_usd"],
                    row["market_cap"],
                    row["volume_24h"],
                    row["percent_change_24h"],
                    row["market_cap_billion"]
                )
            )

        # Get symbols from the current API snapshot
        current_symbols = tuple(df["symbol"].tolist())

        # Remove records that are no longer in the snapshot
        delete_query = """
            DELETE FROM crypto_market_data
            WHERE symbol NOT IN %s
        """

        cursor.execute(
            delete_query,
            (current_symbols,)
        )

        connection.commit()

        print("Data loaded and synchronized successfully.")

        cursor.close()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

        print("Database connection closed.")

if __name__ == "__main__":

    create_table()

    from etl.extract import extract_data
    from etl.transform import transform_data

    # Extract live data from CoinMarketCap
    data = extract_data(limit=3)

    # Transform the API data
    transformed_data = transform_data(data)

    # Load transformed data into PostgreSQL
    load_data(transformed_data)