from src.config import (
    debit_regex,
    debit_exclude,
    amount_regex,
    name_regex,
    categories_regex,
)
import re


def filter_debit_sms(sms):
    for pattern in debit_exclude:
        if re.search(pattern, sms):
            return False
    for pattern in debit_regex:
        if re.search(pattern, sms):
            return True
    return False


def extract_amount(sms, bank_name):
    match = re.search(amount_regex[bank_name], sms)

    if match:
        amount = match.group(1) or match.group(2)
        return float(amount)
    else:
        return None


def extract_name(sms, bank_name):
    match = re.search(name_regex[bank_name], sms)
    if match:
        name = (
            match.group(1)
            or match.group(2)
            or match.group(3)
            or match.group(4)
            or match.group(5)
            or match.group(6)
            or match.group(7)
        )
        return name
    else:
        return None


def categorize(text):
    for category, pattern in categories_regex.items():
        if re.search(pattern, text, re.IGNORECASE):
            return category

    return None
