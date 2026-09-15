import logging

logger = logging.getLogger("cryptopulse")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    logger.addHandler(handler)
    handler.setFormatter(formatter)

# logger.info( "logger test")
# logger.info("CryptoPulse-BI logger started")