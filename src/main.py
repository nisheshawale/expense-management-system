from src.extract import filter_debit_sms, extract_amount, extract_name, categorize
from src.utils import lemmatize
import json
import cProfile


def find_amount_and_category(sms):
    if filter_debit_sms(sms):
        print(sms)
        amount = extract_amount(sms)
        name = extract_name(sms)
        if name is None:
            return amount, "misc", name
        if "@" in name:
            return amount, "individual", name
        else:
            lemmatized_name = lemmatize(name)
            category = categorize(lemmatized_name)

            return amount, category, name
    else:
        return -1, None, None


if __name__ == "__main__":
    json_file = "./data/data.json"
    # profiler = cProfile.Profile()
    # profiler.enable()
    with open(json_file) as fp:
        data = json.load(fp)

    messages = []
    result = []
    for single_phone in data:
        for msg in single_phone["body"]:
            messages.append(msg["body"])
            # try:
            res = find_amount_and_category(msg["body"])
            if res[1] is not None:
                result.append((res))
            # except:
            #     pass
    print(result)
