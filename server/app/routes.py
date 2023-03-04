from flask import Blueprint, jsonify, request, send_from_directory
import os
import db

submission_bp = Blueprint('submission_bp', __name__, url_prefix='/submissions')

SERVER_BASE_URL = 'http://127.0.0.1:5000'


@submission_bp.route('/<filename>', methods=['GET'])
def serve_file(filename):
    if filename.endswith('.pdf'):
        return send_from_directory('../submissions', filename)
    return jsonify(error='Route not found'), 404


@submission_bp.route('/create', methods=['POST'])
def create_submission():
    company_name = request.json.get('company_name')
    physical_address = request.json.get('physical_address')
    annual_revenue = request.json.get('annual_revenue')

    if not company_name or not physical_address or not annual_revenue:
        return jsonify(error='Missing required fields'), 400

    if db.check_submission_for_existence(company_name=company_name, physical_address=physical_address):
        return jsonify(error='Submission already exists'), 409
    try:
        id = db.create_submission(company_name=company_name, physical_address=physical_address,
                                  annual_revenue=annual_revenue)
        return jsonify(message=f'Submission {id} created successfully'), 201
    except Exception as e:
        return jsonify(error='Error on creating submission'), 500


@submission_bp.route('/update/<submission_id>', methods=['PUT'])
def update_submission(submission_id):
    submission = db.get_submission_by_id(submission_id=submission_id)
    if not submission:
        return jsonify(error='Submission not found'), 404

    company_name = request.json.get('company_name', submission.company_name)
    physical_address = request.json.get('physical_address', submission.physical_address)
    annual_revenue = request.json.get('annual_revenue', submission.annual_revenue)
    try:
        db.update_submission(submission_id, company_name, physical_address, annual_revenue)
        return jsonify(message=f'Submission {submission_id} updated successfully'), 200
    except Exception as e:
        return jsonify(error='Error on updating submission'), 500


@submission_bp.route('/get/<submission_id>', methods=['GET'])
def get_submission(submission_id):
    try:
        submission = db.get_submission_by_id(submission_id=submission_id)
        if not submission:
            return jsonify(error='Submission not found'), 404

        submission_dict = submission.__dict__
        del submission_dict["_sa_instance_state"]
        return jsonify(submission_dict), 200
    except Exception as e:
        return jsonify(error=f'Error on getting submission {submission_id}'), 500


@submission_bp.route('/bind/<submission_id>', methods=['PUT'])
def bind_submission(submission_id):
    submission = db.get_submission_by_id(submission_id=submission_id)
    if not submission:
        return jsonify(error='Submission not found'), 404

    signed_application = request.files.get('signed_application').read()

    signed_application_path = f'{SERVER_BASE_URL}/submissions/{submission_id}.pdf'
    app_dir = os.path.abspath('./full_submission_forms')
    file_path = os.path.join(app_dir, f'{submission_id}.pdf')
    with open(file_path, "wb") as f_out:
        f_out.write(signed_application)

    if not signed_application:
        return jsonify(error='Missing signed application file'), 400

    try:
        db.bind_submission(submission_id=submission_id, signed_application_path=signed_application_path)
        return jsonify(message=f'Submission bound successfully {submission_id}'), 200
    except Exception as e:
        return jsonify(error=f'Error on binding submission {submission_id}'), 500


@submission_bp.route('/list', methods=['GET'])
def list_submissions():
    only_bound = bool('True' in request.args.get('only_bound', default='False'))
    submissions = db.list_submissions(only_bound=only_bound)

    submissions_list = []
    for submission in submissions:
        submission_dict = submission.__dict__
        submission_dict.pop('_sa_instance_state')  # Remove SQLAlchemy state info
        submissions_list.append(submission_dict)

    return jsonify(submissions_list), 200
