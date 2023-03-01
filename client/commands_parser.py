def parse_create_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 5:
        raise ValueError("Invalid command format")

    company_name = parts[1]
    physical_address = parts[3]
    annual_revenue = int(parts[4].strip())
    return company_name, physical_address, annual_revenue


def fix_quotation_marks(command_string):
    command_string = command_string.replace('”', '"')
    command_string = command_string.replace('“', '"')
    return command_string


def parse_update_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 7:
        raise ValueError("Invalid command format")

    submission_id = parts[1]
    company_name = parts[3]
    physical_address = parts[5]
    annual_revenue = int(parts[6].strip())
    return submission_id, company_name, physical_address, annual_revenue


def parse_get_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 3:
        raise ValueError("Invalid command format")
    submission_id = parts[1]
    return submission_id


def parse_bind_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 5:
        raise ValueError("Invalid command format")

    submission_id = parts[1]
    signed_application_path = parts[3]
    return submission_id, signed_application_path


def parse_list_submissions_command(command_string):
    return "only_bound" in command_string
