CREATE TABLE IF NOT EXISTS crypto_market_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    price_usd NUMERIC(20, 2) NOT NULL,
    market_cap NUMERIC(30, 2) NOT NULL,
    market_cap_billion NUMERIC(20, 2) NOT NULL,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);