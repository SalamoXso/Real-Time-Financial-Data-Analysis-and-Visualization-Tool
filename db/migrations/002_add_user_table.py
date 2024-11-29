from sqlalchemy import create_engine, Column, Integer, String
from db.models import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

# Create a new database engine
engine = create_engine('postgresql://username:password@localhost/dev_db')

# Create the new table
User.__table__.create(engine)
print("User table migration complete.")
