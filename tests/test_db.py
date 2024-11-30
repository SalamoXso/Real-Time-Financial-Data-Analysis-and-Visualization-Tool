import pytest
import unittest
from db.db_setup import engine
from sqlalchemy.orm import sessionmaker
from db.models import FinancialData

class TestDatabase(unittest.TestCase):
    def test_database_connection(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        data = session.query(FinancialData).first()
        self.assertIsNone(data)  # Assuming the database starts empty
        session.close()

if __name__ == '__main__':
    unittest.main()
