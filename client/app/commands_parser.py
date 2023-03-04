def parse_create_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 5:
        raise ValueError("Invalid command format")
    return parts[1], parts[3], int(parts[4].strip())


def parse_update_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 7:
        raise ValueError("Invalid command format")
    return parts[1], parts[3], parts[5], int(parts[6].strip())


def parse_get_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 3:
        raise ValueError("Invalid command format")
    return parts[1]


def parse_bind_submission_command(command_string):
    command_string = fix_quotation_marks(command_string)
    parts = command_string.split('"')
    if len(parts) != 5:
        raise ValueError("Invalid command format")
    return parts[1], parts[3]


def parse_list_submissions_command(command_string):
    return "only_bound" in command_string


def fix_quotation_marks(command_string):
    return command_string.replace('”', '"').replace('“', '"')
