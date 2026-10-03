import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from config.settings import SCHEDULER_INTERVAL_MINUTES
from etl.run_pipeline import main


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def run_etl():
    """
    Run the CryptoPulse-BI ETL pipeline.
    """

    logger.info("Starting scheduled ETL run...")

    try:
        main()

        logger.info("Scheduled ETL run completed successfully.")

    except Exception:
        logger.exception(
            "Scheduled ETL run failed."
        )


def start_scheduler():
    """
    Start the ETL scheduler.
    """

    scheduler = BlockingScheduler()

    scheduler.add_job(
        run_etl,
        "interval",
        minutes=SCHEDULER_INTERVAL_MINUTES,
        max_instances=1
    )

    logger.info("CryptoPulse-BI scheduler started.")

    logger.info(
        "ETL will run every %s minute(s).",
        SCHEDULER_INTERVAL_MINUTES
    )

    logger.info("Press Ctrl+C to stop the scheduler.")

    try:
        scheduler.start()

    except KeyboardInterrupt:
        logger.info("Scheduler stopped.")


if __name__ == "__main__":
    start_scheduler()