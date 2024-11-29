from db.models import User
from db.db_setup import engine
from sqlalchemy.orm import sessionmaker
from utils.auth.password_hasher import hash_password

# Sample user data
sample_users = [
    User(username='admin', password_hash=hash_password('adminpassword')),
    User(username='user1', password_hash=hash_password('user1password')),
]

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add users to the database
session.bulk_save_objects(sample_users)
session.commit()
session.close()
print("User data seeded successfully.")
