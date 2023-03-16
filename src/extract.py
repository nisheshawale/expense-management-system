from src.config import debit_regex, debit_exclude, amount_regex, name_regex, categories_regex
import re

def filter_debit_sms(sms):
    for pattern in debit_exclude:
        if re.search(pattern, sms):
            return False
    for pattern in debit_regex:
        if re.search(pattern, sms):
            return True
    return False


def extract_amount(sms):
    match = re.search(amount_regex, sms)

    if match:
        amount = float(match.group(1))
        return amount
    else:
        return None


def extract_name(sms):
    match = re.search(name_regex, sms)
    if match:
        name = match.group(1) or match.group(2) or match.group(3) or match.group(4)or match.group(5)
        return name
    else:
        return None


def categorize(text):
    for category, pattern in categories_regex.items():
        if re.search(pattern, text, re.IGNORECASE):
            return category

    return "misc"
