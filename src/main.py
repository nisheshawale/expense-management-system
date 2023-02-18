from src.extract import filter_debit_sms, extract_amount, extract_name, categorize
from src.utils import lemmatize


def main(sms):
    if filter_debit_sms:
        amount = extract_amount(sms)
        name = extract_name(sms)
        if "@" in name:
            return amount, "individual"
        else:
            lemmatized_name = lemmatize(name)
            category = categorize(lemmatized_name)

            return amount, category
    else:
        return -1, None


if __name__ == "__main__":
    sms = "Rs.18.00 is debited from Kotak Bank a/c XXXX3090 to paytm-69696941@paytm on 13-11-22. To report fraud/raise dispute, click kotak.com/fraud. New balance: Rs. 478.00"
    print(main(sms))
