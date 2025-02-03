from extraction import fetch_collections
from load import load_data


def run_etl():
    """
    Runs the entire ETL pipeline: Extract, Transform, Load.
    """
    print("🚀 Starting ETL process...")

    # Step 1: Extract Data
    fetch_collections()

    # Step 2: Load Data (Transformation happens inside load.py)
    load_data()

    print("✅ ETL process completed.")


if __name__ == "__main__":
    run_etl()
