from sqlalchemy import create_engine, Column, Integer, String
from db.models import Base
from sqlalchemy.engine import url

# Create a URL for the database connection
database_url = url.URL(
    "postgresql",
    username="postgres",
    password="HelloHackers1994@*",
    host="localhost",
    database="CoursesPlatform"
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

# Create a new database engine
engine = create_engine(database_url)

# Create the new table
User.__table__.create(engine)
print("User table migration complete.")
