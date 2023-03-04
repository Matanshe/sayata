import random
import string

from sqlalchemy import Column, String, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def generate_id():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8))


class Submission(Base):
    __tablename__ = 'submissions'

    id = Column(String(255), primary_key=True, default=generate_id())
    company_name = Column(String(255), nullable=False)
    physical_address = Column(String(255), nullable=False)
    annual_revenue = Column(Numeric, nullable=False)
    status = Column(Enum('NEW', 'BOUND'), default='NEW', nullable=False)
    signed_application_path = Column(String(255), nullable=True)
