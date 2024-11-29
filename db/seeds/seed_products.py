from db.models import FinancialData
from db.db_setup import engine
from sqlalchemy.orm import sessionmaker

# Sample data to be added
sample_data = [
    FinancialData(symbol='AAPL', timestamp='2024-11-29 14:30', price=175.45, volume=1500),
    FinancialData(symbol='GOOG', timestamp='2024-11-29 14:31', price=2923.25, volume=1000),
]

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add data to the database
session.bulk_save_objects(sample_data)
session.commit()
session.close()
print("Product data seeded successfully.")
