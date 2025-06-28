import re

def is_valid_license_plate(text):

    pattern = r'^(?:[A-Z]{1,2} ?\d{1,4} ?[A-Z]{1,3}|\d{1,2} ?[A-Z]{1,2} ?\d{1,4}|[A-Z]{1,2} ?[A-Z0-9]{1,4}|[A-Z]{1,2}\d{1,4}[A-Z]{0,2})$'
    return re.match(pattern, text.replace(" ", "")) is not None