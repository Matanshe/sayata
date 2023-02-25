from flask import Blueprint, jsonify, request

import db
from models import Submission

submission_bp = Blueprint('submission_bp', __name__, url_prefix='/submissions')


@submission_bp.route('/create', methods=['POST'])
def create_submission():
    company_name = request.json.get('company_name')
    physical_address = request.json.get('physical_address')
    annual_revenue = request.json.get('annual_revenue')

    if not company_name or not physical_address or not annual_revenue:
        return jsonify(error='Missing required fields'), 400

    submission = Submission.query.filter_by(company_name=company_name, physical_address=physical_address).first()
    if submission:
        return jsonify(error='Submission already exists'), 409

    submission = Submission(company_name=company_name, physical_address=physical_address, annual_revenue=annual_revenue)
    db.session.add(submission)
    db.session.commit()

    return jsonify(message=f'Submission {submission.id} created successfully'), 201


@submission_bp.route('/update/<submission_id>', methods=['PUT'])
def update_submission(submission_id):
    submission = Submission.query.filter_by(id=submission_id).first()
    if not submission:
        return jsonify(error='Submission not found'), 404

    submission.company_name = request.json.get('company_name', submission.company_name)
    submission.physical_address = request.json.get('physical_address', submission.physical_address)
    submission.annual_revenue = request.json.get('annual_revenue', submission.annual_revenue)

    db.session.commit()

    return jsonify(message='Submission updated successfully'), 200


@submission_bp.route('/get/<submission_id>', methods=['GET'])
def get_submission(submission_id):
    submission = Submission.query.filter_by(id=submission_id).first()
    if not submission:
        return jsonify(error='Submission not found'), 404

    submission_dict = submission.__dict__
    submission_dict.pop('_sa_instance_state')  # Remove SQLAlchemy state info
    return jsonify(submission_dict), 200


@submission_bp.route('/bind/<submission_id>', methods=['PUT'])
def bind_submission(submission_id):
    submission = Submission.query.filter_by(id=submission_id).first()
    if not submission:
        return jsonify(error='Submission not found'), 404

    signed_application_path = request.json.get('signed_application_path')
    if not signed_application_path:
        return jsonify(error='Missing signed application path'), 400

    submission.signed_application_path = signed_application_path
    submission.status = 'BOUND'

    db.session.commit()

    return jsonify(message='Submission bound successfully'), 200


@submission_bp.route('/list', methods=['GET'])
def list_submissions():
    only_bound = request.args.get('only_bound', default=False, type=bool)

    if only_bound:
        submissions = Submission.query.filter_by(status='BOUND').all()
    else:
        submissions = Submission.query.all()

    submissions_list = []
    for submission in submissions:
        submission_dict = submission.__dict__
        submission_dict.pop('_sa_instance_state')  # Remove SQLAlchemy state info
        submissions_list.append(submission_dict)

    return jsonify(submissions_list), 200
