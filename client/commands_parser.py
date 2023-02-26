def parse_submission_command(command_string):
    command_string = command_string.replace('”', '"')
    command_string = command_string.replace('“', '"')
    parts = command_string.split('"')
    if len(parts) != 5:
        raise ValueError("Invalid command format")

    company_name = parts[1]
    physical_address = parts[3]
    annual_revenue = int(parts[4].strip())
    return company_name, physical_address, annual_revenue
