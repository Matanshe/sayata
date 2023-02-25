from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Enum, LargeBinary

Base = declarative_base()

class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(255), nullable=False)
    physical_address = Column(String(255), nullable=False)
    annual_revenue = Column(Numeric, nullable=False)
    status = Column(Enum('NEW', 'BOUND'), default='NEW', nullable=False)
    signed_application = Column(LargeBinary)
