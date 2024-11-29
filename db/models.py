from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FinancialData(Base):
    __tablename__ = 'financial_data'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)
