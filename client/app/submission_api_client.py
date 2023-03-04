import os

import requests

BASE_URL = "http://127.0.0.1:5000"


def create_submission(company_name, physical_address, annual_revenue):
    payload = {
        "company_name": company_name,
        "physical_address": physical_address,
        "annual_revenue": annual_revenue,
    }
    response = requests.post(f"{BASE_URL}/submissions/create", json=payload)
    if response.status_code == 201:
        submission_id = response.json()["message"].split(" ")[1]
        print(f"Submission {submission_id} created successfully")
    else:
        print(response.json()["error"])


def update_submission(submission_id, company_name, physical_address, annual_revenue):
    payload = {
        "company_name": company_name,
        "physical_address": physical_address,
        "annual_revenue": annual_revenue,
    }
    response = requests.put(f"{BASE_URL}/submissions/update/{submission_id}", json=payload)
    if response.status_code == 200:
        print(f"Submission {submission_id} updated successfully")
    else:
        print(response.json()["error"])


def get_submission(submission_id):
    response = requests.get(f"{BASE_URL}/submissions/get/{submission_id}")
    if response.status_code == 200:
        submission_data = response.json()
        print(submission_data)
    else:
        print(response.json()["error"])


def bind_submission(submission_id, signed_application_path):
    home_dir = os.path.expanduser("~")
    full_signed_application_path = os.path.join(home_dir, "/".join(signed_application_path.split("/")[1:]))
    with open(full_signed_application_path, "rb") as f:
        files = {
            "signed_application": (os.path.basename(signed_application_path), f, "application/pdf"),
        }
        response = requests.put(f"{BASE_URL}/submissions/bind/{submission_id}", files=files)
    if response.status_code == 200:
        print(f"Successfully bound submission {submission_id}")
    else:
        print(response.json()["error"])


def list_submissions(only_bound=False):
    params = {"only_bound": only_bound}
    response = requests.get(f"{BASE_URL}/submissions/list", params=params)
    if response.status_code == 200:
        submissions = response.json()
        for submission in submissions:
            print(f"Submission Id: {submission.get('id')}")
            print(f"Company Name: {submission.get('company_name')}")
            print(f"Physical Address: {submission.get('physical_address')}")
            print(f"Annual Revenue: {submission.get('annual_revenue')}")
            print(f"Status: {submission.get('status')}")
            print(f"Signed Application: {submission.get('signed_application_path')}")
            print("=" * 30)
    else:
        print(response.json()["error"])
