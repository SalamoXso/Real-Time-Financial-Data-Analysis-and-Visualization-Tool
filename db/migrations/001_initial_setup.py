from sqlalchemy import create_engine
from sqlalchemy.engine import url
from db.models import Base

# Create a URL for the database connection
database_url = url.URL(
    "postgresql",
    username="postgres",
    password="HelloHackers1994@*",
    host="localhost",
    database="CoursesPlatform"
)

# Create the engine, but do not connect to the database yet
engine = create_engine(database_url)

# Check if the database exists, if not create it
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.engine import reflection

inspector = reflection.Inspector.from_engine(engine)
if 'dev_db' not in inspector.get_schema_names():
    # If the database does not exist, create it
    with engine.begin() as conn:
        conn.execute("CREATE DATABASE dev_db")

# Now connect to the newly created database
engine.dispose()
engine = create_engine(database_url)

# Create tables in the database
Base.metadata.create_all(engine)
print("Initial migration complete.")