from src.extract import filter_debit_sms, extract_amount, extract_name, categorize
from src.utils import lemmatize
import requests
import json
import cProfile


def find_amount_and_category(sms):
    if filter_debit_sms(sms):
        amount = extract_amount(sms)
        name = extract_name(sms)
        if name is None:
            return amount, 'misc'
        if "@" in name:
            return amount, "individual"
        else:
            lemmatized_name = lemmatize(name)
            category = categorize(lemmatized_name)

            return amount, category
    else:
        return -1, None


if __name__ == "__main__":
    json_file = "./data/data.json"
    # profiler = cProfile.Profile()
    # profiler.enable()
    with open(json_file) as fp:
        data = json.load(fp)

    messages = []
    result = []

    for i, single_phone in enumerate(data):
        for j, msg in enumerate(single_phone['body']):
            try:
                res = find_amount_and_category(msg['body'])
                if res[1] is not None:
                    messages.append(msg['body'])
                    result.append((res))

            except:
                    pass

    print(result)
    print(len(messages), len(result))
    # profiler.disable()
    # profiler.dump_stats("example.stats")

