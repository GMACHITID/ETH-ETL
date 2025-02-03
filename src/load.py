from sqlalchemy.orm import Session
from database import SessionLocal, Collection
from transformation import transform_data

def load_data():
    """
    Loads transformed data into PostgreSQL.
    """
    transformed_data = transform_data()
    if not transformed_data:
        print("No data to load.")
        return

    session = SessionLocal()
    try:
        existing_collections = {c.collection for c in session.query(Collection.collection).all()}
        for data in transformed_data:
            if data["collection"] in existing_collections:
                print(f"Warning: Skipping duplicate: {data['collection']}")
                continue  # Skip inserting duplicate data

            new_collection = Collection(
                collection=data["collection"],
                name=data["name"],
                description=data["description"],
                image_url=data["image_url"],
                owner=data["owner"],
                twitter_username=data["twitter_username"],
                contracts=data["contracts"],
            )
            session.add(new_collection)

        session.commit()
        print(f"Nice! {len(transformed_data)} records successfully loaded into PostgreSQL.")
    except Exception as e:
        session.rollback()
        print(f"Error inserting data: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    load_data()