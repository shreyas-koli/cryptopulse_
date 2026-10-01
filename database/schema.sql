CREATE TABLE IF NOT EXISTS crypto_market_data (
    id SERIAL PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    symbol VARCHAR(20) NOT NULL UNIQUE,

    rank INTEGER NOT NULL,

    price_usd NUMERIC(20, 8) NOT NULL,

    market_cap NUMERIC(30, 2) NOT NULL,

    volume_24h NUMERIC(30, 2) NOT NULL,

    percent_change_24h NUMERIC(10, 4) NOT NULL,

    market_cap_billion NUMERIC(20, 4) NOT NULL,

    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);