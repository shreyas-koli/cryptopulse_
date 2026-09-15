import subprocess
import sys


def run_step(step_name, command):
    """
    Run one ETL step and display its status.
    """

    print(f"\nStarting {step_name}...")

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"{step_name} failed.")
        sys.exit(1)

    print(f"{step_name} completed successfully.")


def main():
    """
    Run the complete ETL pipeline.
    """

    run_step(
        "Extraction",
        [sys.executable, "-m", "etl.extract"]
    )

    run_step(
        "Transformation",
        [sys.executable, "-m", "etl.transform"]
    )

    run_step(
        "Loading",
        [sys.executable, "-m", "etl.load"]
    )

    print("\nComplete ETL pipeline executed successfully.")


if __name__ == "__main__":
    main()