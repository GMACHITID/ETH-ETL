import pandas as pd
import json


RAW_DATA_PATH = "data/raw/opensea_collections.json"

def transform_data():
    """
    Reads raw JSON data, extracts relevant fields using Pandas, and structures it for database insertion.

    Returns a list of transformed collection dictionaries.
    """
    try:
        with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Convert JSON into DataFrame
        df = pd.DataFrame(raw_data.get("collections", []))

        # Define expected columns and their default values
        expected_columns = {
            "slug": "Unknown",
            "name": "Unnamed Collection",
            "description": "",
            "image_url": "",
            "safelist_request_status": "",  # Owner field
            "twitter_username": "",
            "primary_contracts": None
        }

        # Assign default values only for missing columns
        for col, default_value in expected_columns.items():
            if col not in df.columns:
                if default_value is None:
                    df[col] = [[] for _ in range(len(df))]  # Create separate empty lists for each row
                else:
                    df[col] = default_value  # Assign default value directly

        # Rename columns to match database schema
        df.rename(columns={
            "slug": "collection",
            "safelist_request_status": "owner",
            "primary_contracts": "contracts"
        }, inplace=True)

        # Convert DataFrame to list of dictionaries
        transformed_data = df.to_dict(orient="records")

        return transformed_data

    except FileNotFoundError:
        print("❌ Raw data file not found.")
        return []

if __name__ == "__main__":
    transformed_db_data = transform_data()
    print(f"✅ Transformed {len(transformed_db_data)} collections using Pandas.")
