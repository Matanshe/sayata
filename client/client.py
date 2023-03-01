import requests
import os

import submission_management.client.commands_parser as parser

BASE_URL = "http://localhost:5000"

history = []


def create_submission(company_name, physical_address, annual_revenue):
    payload = {
        "company_name": company_name,
        "physical_address": physical_address,
        "annual_revenue": annual_revenue
    }
    response = requests.post(f"{BASE_URL}/submissions/create", json=payload)
    if response.status_code == 201:
        submission_id = response.json().get("message").split(" ")[1]
        print(f"Submission {submission_id} created successfully")
        history.append(f"CREATE SUBMISSION {company_name} {physical_address} {annual_revenue}")
    else:
        print(response.json().get("error"))


def update_submission(submission_id, company_name, physical_address, annual_revenue):
    payload = {}
    payload["company_name"] = company_name
    payload["physical_address"] = physical_address
    payload["annual_revenue"] = annual_revenue

    response = requests.put(f"{BASE_URL}/submissions/update/{submission_id}", json=payload)
    if response.status_code == 200:
        print(f"Submission {submission_id} updated successfully")
        history.append(f"UPDATE SUBMISSION {submission_id} {company_name} {physical_address} {annual_revenue}")
    else:
        print(response.json().get("error"))


def get_submission(submission_id):
    response = requests.get(f"{BASE_URL}/submissions/get/{submission_id}")
    if response.status_code == 200:
        submission_data = response.json()
        print(submission_data)
        history.append(f"GET SUBMISSION {submission_id}")
    else:
        print(response.json().get("error"))


def bind_submission(submission_id, signed_application_path):
    home_dir = os.path.expanduser("~")
    full_signed_application_path = os.path.join(home_dir, '/'.join(signed_application_path.split('/')[1:]))
    with open(full_signed_application_path, "rb") as f:
        files = {"signed_application": (os.path.basename(signed_application_path), f, "application/pdf")}
        response = requests.put(f"{BASE_URL}/submissions/bind/{submission_id}", files=files)
    if response.status_code == 200:
        print(f"Successfully bound submission {submission_id}")
        history.append(f"BIND SUBMISSION {submission_id} {signed_application_path}")
    else:
        print(response.json().get("error"))


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
            print("===" * 10)
        history.append(f"LIST SUBMISSIONS only_bound: {only_bound}")
    else:
        print(response.json().get("error"))


if __name__ == '__main__':
    while True:
        command = input("Enter a command: ")
        try:
            if command.startswith("CREATE SUBMISSION"):
                company_name, physical_address, annual_revenue = parser.parse_create_submission_command(command)
                create_submission(company_name, physical_address, annual_revenue)
            elif command.startswith("UPDATE SUBMISSION"):
                submission_id, company_name, physical_address, annual_revenue = parser.parse_update_submission_command(
                    command)
                update_submission(submission_id, company_name, physical_address, annual_revenue)
            elif command.startswith("GET SUBMISSION"):
                submission_id = parser.parse_get_submission_command(command)
                get_submission(submission_id)
            elif command.startswith("BIND SUBMISSION"):
                submission_id, signed_application_path = parser.parse_bind_submission_command(command)
                bind_submission(submission_id, signed_application_path)
            elif command.startswith("LIST SUBMISSION"):
                only_bound = parser.parse_list_submissions_command(command)
                list_submissions(only_bound)
            elif command.startswith("HISTORY"):
                for command in history:
                    print(command)
            elif command == "exit":
                break
            else:
                print("Invalid command")
        except ValueError as e:
            print(e)
