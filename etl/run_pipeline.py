from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import create_table, load_data


def main():
    """
    Run the complete CryptoPulse-BI ETL pipeline.
    """

    print("\n========== CRYPTOPULSE-BI ETL PIPELINE ==========")

    # -------------------------------------------------
    # 1. Create database table
    # -------------------------------------------------

    print("\n[1/4] Checking database table...")

    create_table()

    print("Database table ready.")

    # -------------------------------------------------
    # 2. Extract
    # -------------------------------------------------

    print("\n[2/4] Extracting data from CoinMarketCap...")

    data = extract_data(limit=3)

    print(
        f"Successfully extracted {len(data)} cryptocurrencies."
    )

    # -------------------------------------------------
    # 3. Transform
    # -------------------------------------------------

    print("\n[3/4] Transforming cryptocurrency data...")

    transformed_data = transform_data(data)

    print("Transformation completed successfully.")

    # -------------------------------------------------
    # 4. Load
    # -------------------------------------------------

    print("\n[4/4] Loading data into PostgreSQL...")

    load_data(transformed_data)

    print("\n========== PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    main()