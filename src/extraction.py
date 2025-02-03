import requests
import json
import os
from config import API_URL, HEADERS

RAW_DATA_DIR = "data/raw/"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def fetch_collections(chain="ethereum", limit=50):
    """
    Fetches collections from the OpenSea API for the specified blockchain.

    Parameters:
        chain (str): The blockchain to filter by (default: "ethereum").
        limit (int): The number of collections to fetch per request.

    Return a list of collection data.
    """
    params = {"chain": chain, "limit": limit}
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params)
        response.raise_for_status()  # Raise an error for HTTP failures
        data = response.json()

        # Save raw JSON
        file_path = os.path.join(RAW_DATA_DIR, "opensea_collections.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Data successfully extracted and saved to {file_path}")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error during API extraction: {e}")
        return []

if __name__ == "__main__":
    fetch_collections()