import logging
import os

import requests
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# CoinMarketCap API URL
API_URL = (
    "https://pro-api.coinmarketcap.com/"
    "v3/cryptocurrency/listings/latest"
)


# Create logger
logger = logging.getLogger(__name__)


def extract_data(limit=10):
    """
    Fetch cryptocurrency market data
    from CoinMarketCap API.
    """

    # Get API key from .env
    api_key = os.getenv("COINMARKETCAP_API_KEY")

    if not api_key:
        logger.error(
            "CoinMarketCap API key is missing."
        )

        raise ValueError(
            "COINMARKETCAP_API_KEY is not set."
        )

    # API request headers
    headers = {
        "Accept": "application/json",
        "X-CMC_PRO_API_KEY": api_key
    }

    # API request parameters
    params = {
        "start": 1,
        "limit": limit,
        "convert": "USD"
    }

    try:

        logger.info(
            "Requesting cryptocurrency data from CoinMarketCap."
        )

        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=30
        )

        # Raise an error if HTTP request failed
        response.raise_for_status()

        # Convert response to Python dictionary
        response_data = response.json()

        # Get cryptocurrency list
        data = response_data.get("data", [])

        if not data:

            logger.warning(
                "CoinMarketCap API returned no data."
            )

            return []

        logger.info(
            "Successfully extracted %d cryptocurrencies.",
            len(data)
        )

        return data

    except requests.exceptions.Timeout:

        logger.error(
            "CoinMarketCap API request timed out."
        )

        raise

    except requests.exceptions.HTTPError as error:

        logger.error(
            "CoinMarketCap API returned HTTP error: %s",
            error
        )

        raise

    except requests.exceptions.RequestException as error:

        logger.error(
            "CoinMarketCap API request failed: %s",
            error
        )

        raise


# This part runs only when extract.py
# is executed directly.
if __name__ == "__main__":

    data = extract_data(limit=3)

    print(
        f"Successfully extracted {len(data)} cryptocurrencies."
    )

    for coin in data:

        print(
            coin["cmc_rank"],
            coin["name"],
            coin["symbol"]
        )