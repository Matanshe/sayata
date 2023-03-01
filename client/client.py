import requests

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
        history.append(f"create_submission {company_name} {physical_address} {annual_revenue}")
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
        history.append(f"update_submission {submission_id} {company_name} {physical_address} {annual_revenue}")
    else:
        print(response.json().get("error"))


def get_submission(submission_id):
    response = requests.get(f"{BASE_URL}/submissions/get/{submission_id}")
    if response.status_code == 200:
        submission_data = response.json()
        print(submission_data)
        history.append(f"get_submission {submission_id}")
    else:
        print(response.json().get("error"))


def bind_submission(submission_id, signed_application_path):
    with open(signed_application_path, "rb") as f:
        files = {"signed_application": f}
        response = requests.put(f"{BASE_URL}/submissions/bind/{submission_id}", files=files)
    if response.status_code == 200:
        print("Submission bound successfully")
        history.append(f"bind_submission {submission_id} {signed_application_path}")
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

        except ValueError as e:
            print(e)