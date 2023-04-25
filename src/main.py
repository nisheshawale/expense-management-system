from src.extract import filter_debit_sms, extract_amount, extract_name, categorize
from src.utils import lemmatize
import json
import cProfile


def find_amount_and_category(sms, bank_name):
    if filter_debit_sms(sms):
        amount = extract_amount(sms, bank_name)
        name = extract_name(sms, bank_name)
        if name is None:
            return amount, "misc", name
        # if "@" in name:
        #     return amount, "individual", name
        else:
            lemmatized_name = lemmatize(name)
            category = categorize(lemmatized_name)
            if category:
                return amount, category, name
            elif "@" in name:
                return amount, "individual", "name"
            else:
                return amount, "misc", name
    else:
        return -1, None, None


if __name__ == "__main__":
    # json_file = "./data/data.json"
    # # profiler = cProfile.Profile()
    # # profiler.enable()
    # with open(json_file) as fp:
    #     data = json.load(fp)

    # # messages = []
    # result = []
    # for single_phone in data:
    #     for msg in single_phone["body"]:
    #         # messages.append(msg["body"])
    #         # try:
    #         res = find_amount_and_category(msg["body"])
    #         if res[1] is not None:
    #             result.append((res))
    #         # except:
    #         #     pass
    result = []
    bank_name = "paytm"
    sms_sbi = "Dear SBI User, your A/c X9864-debited by Rs3000.0 on 27Mar23 transfer to BISHAL NAYAK Ref No 308669542415. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"
    sms_sbi2 = "Dear SBI User, your A/c X5587-debited by Rs160.0 on 31Jul22 transfer to ECOMEXPRESS Ref No 221216108195. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"
    sms_sbi3 = "Dear SBI User, your A/c X5587-debited by Rs140.0 on 14Jun22 transfer to GLORY A Ref No 216515381781. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"
    sms_sbi4 = "Dear SBI User, your A/c X7199-debited by Rs1000.0 on 26Feb23 transfer to PUSHPAM KUMAR Ref No 342327382993. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"
    sms_boi = "BOI UPI - Your VPA 821012058@ybl linked to Bank of India a/c no. XXXXXXXXXXX5504 is debited for Rs.90.00 and credited to 7238824321@ybl (UPI Ref no 226889029830)."
    sms_hdfc = "HDFC Bank: Rs 20.00 debited from a/c **2209 on 31-12-22 to VPA BHARATPE90723849218@yesbankltd(UPI Ref No 236552648806). Not you? Call on 18002586161 to report"
    sms_hdfc2 = "HDFC Bank: Rs 111.00 debited from a/c **2209 on 23-12-22 to VPA swiggystores@icici(UPI Ref No 235723974750). Not you? Call on 18002586161 to report"
    sms_icici = "ICICI Bank Acct XX933 debited with Rs 300.00 on 23-Mar-22 & Acct XX587 credited.IMPS:208210005514. Call 18002662 for dispute or SMS BLOCK 933 to 9215676766"
    sms_icici2 = "INR 1,045.00 spent on ICICI Bank Card XX0000 on 19-Mar-23 at Amazon.in - Gro. Avl Lmt: INR 1,14,882.90. To dispute,call 18002662/SMS BLOCK 0000 to 9215676766"
    sms_paytm = "You have sent Rs.1 to Abhishek Kumar Sharma using Paytm App. UPI Reference: 103966415348 :PPBL"
    sms_paytm2 = "Rs.10.00 sent to paytmqr28100505010117rjbef46ts from PPBL a/c 91XX2627. UPI Ref:229634965573. Balance:https://m.paytm.me/pbCheckBal. Query:http://m.p-y.tm/care"
    sms_paytm3 = "You have paid Rs.120.00 via a/c 91XX4862 to SHOBHA HOME NEEDS on 26-03-2023. Ref:3105414981. Queries? Click http://m.paytm.me/care :PPBL"
    sms_paytm4 = "You have paid Rs.150.00 via a/c 91XX1688 to HP AUTO CARE CENTRE HBR LAYOU on 14-03-2023. Ref:3075207470. Queries? Click http://m.paytm.me/care :PPBL"
    sms_paytm5 = "You have paid Rs.149.00 via a/c 91XX1688 to Paytm Add Money on 13-03-2023. Ref:3073936736. Queries? Click http://m.paytm.me/care :PPBL"
    sms_paytm6 = "Rs.25.00 sent to jio@citibank from your Paytm a/c 91XX6097. Ref: 218789722367. View your past payments at https://m.paytm.me/msg :PPBL"
    sms_ind = "Your VPA nirbh49@okicici linked to Indian Bank a/c no. XXXXXXX6980 is debited for Rs.50.00 and credited to suryaragul000-1@oksbi (UPI Ref no 308860027300).-Indian Bank"
    res = find_amount_and_category(sms_paytm6, bank_name)
    if res[1] is not None:
        result.append((res))
    print(result)
