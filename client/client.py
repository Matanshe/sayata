import requests

from submission_management.client.commands_parser import parse_submission_command

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


if __name__ == '__main__':
    while True:
        command = input("Enter a command: ")
        try:
            if command.startswith("CREATE SUBMISSION"):
                company_name, physical_address, annual_revenue = parse_submission_command(command)
                create_submission(company_name, physical_address, annual_revenue)

        except ValueError as e:
            print(e)
