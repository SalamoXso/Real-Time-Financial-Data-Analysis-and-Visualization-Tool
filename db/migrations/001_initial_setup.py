from sqlalchemy import create_engine
from db.models import Base

# Create a new database engine
engine = create_engine('postgresql://username:password@localhost/dev_db')

# Create tables in the database
Base.metadata.create_all(engine)
print("Initial migration complete.")
