from sqlalchemy import create_engine
from config.config import config

# Create a database engine using the DATABASE_URI from the config
engine = create_engine(config.get('DATABASE_URI'))

def create_tables():
    # Add logic to create tables based on models
    pass

if __name__ == "__main__":
    create_tables()
