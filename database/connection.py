import os

import psycopg2
from dotenv import load_dotenv


# Load variables from the .env file
load_dotenv()

# Read PostgreSQL connection settings
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_connection():
    """
    Create and return a connection to PostgreSQL.
    """

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    return connection


if __name__ == "__main__":
    connection = get_connection()

    print("PostgreSQL connection successful.")

    connection.close()

    print("PostgreSQL connection closed.")