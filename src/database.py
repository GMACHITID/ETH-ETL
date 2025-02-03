from sqlalchemy import create_engine, Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "etl_user"
DB_PASSWORD = "I hid my DB password for the project as well"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "opensea_etl"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Engine & session for database

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    collection = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
    owner = Column(String(255), nullable=True)
    twitter_username = Column(String(255), nullable=True)
    contracts = Column(JSON, nullable=True)  # Store contract details as JSON


def init_db():
    Base.metadata.create_all(engine)   #Create the table

if __name__ == "__main__":
    init_db()
    print("Database and tables created.")