import os
import pandas as pd
from pathlib import Path

from dotenv import load_dotenv
from database.connection import get_connection

load_dotenv()

PROCESSED_FILE = "data/processed/transformed_crypto.csv"

SCHEMA_FILE = "database/schema.sql"

def create_table():
    schema_path = Path(SCHEMA_FILE)
    schema_sql = schema_path.read_text()
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(schema_sql)
        connection.commit()
        print("Table created succesfully")
        cursor.close()

    finally: 
        connection.close()
        print("Database connection closed.")


def load_data(df):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        insert_query = """
         INSERT INTO crypto_market_data (
                name,
                symbol,
                price_usd,
                market_cap,
                market_cap_billion
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (symbol) DO NOTHING
        """

        for _, row in df.iterrows():
            cursor.execute(
                insert_query,
                (
                    row["name"],
                    row["symbol"],
                    row["price_usd"],
                    row["market_cap"],
                    row["market_cap_billion"]
                )
            )

        connection.commit()
        print("data loaded succesfully.")
        cursor.close()

    finally:
        connection.close()
        print("Database connection closed")

if __name__ == "__main__":
    create_table()

    df = pd.read_csv(PROCESSED_FILE)
    load_data(df)