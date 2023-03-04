from submission_api_client import (
    create_submission,
    update_submission,
    get_submission,
    bind_submission,
    list_submissions
)
from commands_parser import (
    parse_create_submission_command,
    parse_update_submission_command,
    parse_get_submission_command,
    parse_bind_submission_command,
    parse_list_submissions_command,
)

history = []

if __name__ == '__main__':
    while True:
        command = input("Enter a command: ")
        try:
            if command.startswith("CREATE SUBMISSION"):
                company_name, physical_address, annual_revenue = parse_create_submission_command(command)
                create_submission(company_name, physical_address, annual_revenue)
                history.append(f"CREATE SUBMISSION {company_name} {physical_address} {annual_revenue}")
            elif command.startswith("UPDATE SUBMISSION"):
                submission_id, company_name, physical_address, annual_revenue = parse_update_submission_command(
                    command)
                update_submission(submission_id, company_name, physical_address, annual_revenue)
                history.append(f"UPDATE SUBMISSION {submission_id} {company_name} {physical_address} {annual_revenue}")
            elif command.startswith("GET SUBMISSION"):
                submission_id = parse_get_submission_command(command)
                get_submission(submission_id)
                history.append(f"GET SUBMISSION {submission_id}")
            elif command.startswith("BIND SUBMISSION"):
                submission_id, signed_application_path = parse_bind_submission_command(command)
                bind_submission(submission_id, signed_application_path)
                history.append(f"BIND SUBMISSION {submission_id} {signed_application_path}")
            elif command.startswith("LIST SUBMISSION"):
                only_bound = parse_list_submissions_command(command)
                list_submissions(only_bound)
                history.append(f"LIST SUBMISSIONS only_bound: {only_bound}")
            elif command.startswith("HISTORY"):
                for command in history:
                    print(command)
            elif command == "exit":
                print('Bye Bye')
                break
            else:
                print("Invalid command")
        except ValueError as e:
            print(e)
