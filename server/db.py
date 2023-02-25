from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Submission

engine = create_engine('sqlite:///submissions.db')
Session = sessionmaker(bind=engine)
session = Session()


def create_submission(company_name, physical_address, annual_revenue):
    submission = Submission(
        company_name=company_name,
        physical_address=physical_address,
        annual_revenue=annual_revenue,
    )
    session.add(submission)
    session.commit()

    return submission.id


def get_submission(submission_id):
    submission = session.query(Submission).get(submission_id)
    if not submission:
        raise ValueError(f"Submission with ID {submission_id} not found")

    return submission


def update_submission(submission_id, company_name, physical_address, annual_revenue):
    submission = get_submission(submission_id)
    submission.company_name = company_name
    submission.physical_address = physical_address
    submission.annual_revenue = annual_revenue
    session.commit()


def bind_submission(submission_id, signed_application):
    submission = get_submission(submission_id)
    submission.status = "BOUND"
    submission.signed_application = signed_application
    session.commit()


def list_submissions(only_bound=False):
    submissions = session.query(Submission).all()
    if only_bound:
        submissions = [s for s in submissions if s.status == "BOUND"]

    return submissions
