debit_regex = [
    "^Recharge of INR (\d+\.\d+) is successful",
    "^Paid Rs\.[0-9]*\.?[0-9]+ via a/c [a-zA-Z0-9]+ to",
    "^Rs\.[0-9]+\.[0-9]{2} sent to [a-zA-Z0-9!@#$%^&*.]+ from [a-zA-Z0-9]+ a/c [a-zA-Z0-9]",
    "^You have paid Rs\.[0-9]+\.[0-9]{2} via a/c [a-zA-Z0-9 ]+ to",
    "^Sent Rs\.[0-9]+\.[0-9]{2} from [a-zA-Z0-9 ]+ to",
    "you[\s\S]{0,40}debited|debited[\s\S]{0,30}in[^\w]*your?[^a-z]",
    "(debited|thank.*using)[\s\S]*your[\s\S]{0,40}debit[^\w]*card",
    "(debited|sent[^\w]*to)[\s\S]{0,30}from[^\w]*your?[^a-z]",
    "(debited|sent[^\w]*to)[\s\S]{0,30}from[^\w]",
    "^[\s\S]{0,20}spent[^\w]*on.{0,20}card[^a-z]|wi?thdra?wn?[^\w]*from[^a-z]",
    "your[^\w]*vpa[\s\S]*debited[\s\S]*by[^\w]*vpa|^[\s\S]{0,20}bank[^\w]*a[c/]c.*debited",
    "spent.{0,20}via[^\w]*debit[^\w]*card|debit[^\w]*t[rx]a?ns?a?c?t?i?o?n?s?[^a-z].*on[^a-z].*from[^a-z]",
    "a[c/]c.*debited[^\w]*with[^a-z]|^[\s\S]{0,20}\d+[^\w]*dr[^\w]",
    "(debit|used at|[^a-z]dr[^a-z])[\s\S]*[^a-z]wi?t?h?dr?a?w?l[^a-z]|[^a-z]wi?t?h?dr?a?w?l[^a-z][\s\S]*(debit|used at|[^a-z]dr[^a-z])",
    "a[c/]c.{0,20}debit:|linked[^\w]*to[\s\S]*debited|(?<=debited).*credited|(withdrawn|spent).*debit[^\w]*a?t?m?[^\w]*card",
    "a[c/]?c[^a-z].{0,20}debited[^\w]*with.*thr?o?ug?h?|[^a-z]pos[^a-z]|used (at|on) atm",
    "debited.*towards?.*[^a-z]by[^a-z]|cash[^\w]*withdra?wa?l.*card[^a-z].*on[^a-z]",
    "debited.*[^a-z]a[c/]c.*cheque|^[\s\S]{0,30}a[c/]c.*debited.*on[^a-z]|cheque.*debited",
    "^boi[\s\S]*debited|(txn|trn|transaction)s?[^a-z].*[^a-z]to[^a-z].*completed|[^a-z]cwdr[^a-z]",
    "^update.*debited from|thank.*using.*(debit|atm|debit[^\w]*atm)[^\w]*card",
    "savings?[^\w]*no.*debited[^\w]*with|(sent|debited).*from[^\w]*your[^\w]*a[c/]c",
    "w/d.*atm.*fm.*a[c/]c.*on|withdrawn[^\w]*at.*atm.*on.*from|withdrawn[\s\S]*atm[^\w]*id",
    "paid.*at.*using[^\w]*debit[^\w]*card|^[\s\S]{0,30}debited[^\w]*from.*[^a-z]*on[^a-z]",
    "^[\s\S]{0,30}debited.*[^a-z]via[^a-z].*debit[^\w]*card|pos[^\w]*(transaction|txn)s?.*made.*on[^\w]*your",
    "upi[^\w]*payment.*sent[^\w]*to[^a-z]|debited.*to[^\w]*sb[^a-z].*bal:.*on|^[^\w]*paid[^a-z][\s\S]*using[^a-z]",
    "debited[^\w]*from[^\w]*a[c/]c.*towards?|debited[^\w]*to[^\w]*a[c/]c.*on[^a-z]",
    "sent[^\w]*from[^\w]*your.*a[c/]c.*[^a-z]to[^a-z]|^[\s\S]{0,20}debited[^\w]*to[^\w]*ac[^a-z].*on",
    "pos[^\w]*(transaction|tran|txn)s?[^a-z].*is[^a-z].*on[^a-z]",
    "you[^\w]*[ha']*ve[^\w]*paid.*using.*debit[^\w]*card|withdrawn.*at[^a-z].*atm[^a-z].*from",
    "^[^\w]*debited.*from[^\w]*a[c/]c|purchase.*made.*debit[^\w]*card|made.*payment.*from.*your.*bank",
    "^[\s\S]{0,20}debited[^\w]*for[^a-z].*upi[^a-z]|made.*purchase.*for.*on",
    "wi?t?h?dr?a?w?l[^\w]*of.*on[^a-z].*fro?m[^\w]*a[c/]?c[^a-z]|you[^\w]*[ha']*ve[^\w]*sent.*to[^a-z].*upi",
    "^[\s\S]{0,20}paid.*using.{0,20}debit[^\w]*card|made.*purchase.*using.*debit[^\w]*card",
    "your[^\w]*a[c/]c.*is[^\w]*dr[^\w]*for|debited.*[^a-z]to[^a-z].*your[^\w]*a[c/]c",
    "quick[^\w]*transfer.*to[^a-z].*completed|^a[c/]c[^\w]+\w+[^\w]*debited[^\w]*for[^a-z]",
    "^ac[^a-z][^\w]*\w+[^\w]*debited[^\w]*by[^a-z]|^card.*used.*for.*ecom",
    "rec[ei]*ved.*payment[^\w]*of.*from[^a-z].*txn[^\w]*id[^a-z]|paid.*by.*bhim.*upi.*at[^a-z]",
    "imps[^\w]*txn[^\w]*status[^\w]*success|neft[^\w]*payment[^\w]*with[^\w]*utr",
    "you.*sent.*[^a-z]to[^a-z].*using.*your.*[^a-z]upi[^a-z]",
    "(transaction|txn)s?[^\w]*of.{0,20}done[^\w]*via[^\w]*debit[^\w]*card",
    "your[^\w]*neft[^\w]*r?t?g?s?[^\w]*utr[^\w]*no.*benificery|transferred.*imps[^\w]*ref.*(benificery|beneficiary)",
    "your[^\w]*fund[^\w]*transfer.*(benificery|beneficiary).*is[^\w]*success",
    "you[^\w]*[ha']*ve.*transferred.*to[^\w]*a[c/]c.*via[^\w]*neft",
    "your.*neft.*ref.*credited[^\w]*to[^\w]*(benificery|beneficiary)|made.*debit[^\w]*card.*purchase",
    "debit[^\w]*card.*used.*ecom.*at[^a-z]|sent[^\w]*to.*from[^\w]*your.*a[c/]c.*upi[^a-z]",
    "your[^\w]*imps.*[^a-z]to[^a-z].*a[c/]c.*credited|withdrawn[\s\S]*atm[^a-z]",
    "neft.*with[^\w]*utr.*credited.*(benificery|beneficiary)|(transaction|txn)s?.*made.*card.*atm[^a-z]",
    "transferred[^\w]*fro?m[^\w]*a[c/]c.*to:|your.*a[c/]c.*had.*[^a-z]atm[^a-z]",
    "your.*a[c/]c.*had.*\d+[^\w]*dr[^\w]*on[^a-z]|a[c/]c[\s\S]*debited[^\w]*vide[^\w]*che?qu?e?[^\w]*no",
    "^[^\w]*(your|yr|ur)[^a-z].*[^a-z]upi[^\w]*(transaction|txn)s?[^a-z].*fro?m[^a-z].*not[^\w]*y?o?u[^a-z]",
    "[^a-z]paid.*a[c/]c.*vide[^\w]*che?qu?e?[^\w]*no|debit[^\w]*fr?o?m[^\w]*a[c/]c.*at.*atm[^a-z]",
    "(your|yr|ur)[^a-z].*debit[^\w]*(cash|transfer|.*neft)[^a-z]|^imps[^\w]*transfer.*[^a-z]to[^a-z].*[^a-z]for[^a-z].*completed",
]

debit_exclude = [r"\bwill\sbe\sdebited\b"]

# amount regex for different banks
amount_regex = {
    "sbi": "Rs\.?\s?(\d+\.?\d*)",
    "boi": "Rs\.?\s?(\d+\.?\d*)",
    "hdfc": "Rs\.?\s?(\d+\.?\d*)",
    "icici": "Rs\.?\s?(\d+\.?\d*)|INR\.?\s?(\d+\.?\d*)",
    "paytm": "Rs\.?\s?(\d+\.?\d*)",
    "ind": "Rs\.?\s?(\d+\.?\d*)",
}
## amount_regex = "(?:(?<=Rs)|(?<=Rs\.))\d+\.\d+"
# amount_regex = "Rs\.?\s?(\d+\.?\d*)|INR\.?\s?(\d+\.?\d*)"

# Name regex for different banks
name_regex = {
    "sbi": "transfer to (.*?) Ref",
    "boi": "credited to (.*?) (\(UPI )?-?Ref",
    "hdfc": "to VPA (.*?) ?\(UPI",
    "icici": "at (.*?). Avl Lmt|& (.*?) credited",
    "paytm": "sent to (.*?) from|to (.*?) on|to (.*?) using",
    "ind": "credited to (.*?) \(UPI",
}
# name_regex = "to (.*?) on|to (.*?) from|to (.*?) Ref|credited to (.*?) -Ref|; (.*?) credited|for your (.*?) on|^(BOIMobile) -"


categories_regex = {
    "food": r"(yummy|sweet|swiggy |zomato|food|taste|restaurant|tea|coffee|domino|pizza|meat|fish|chicken|dairy|rolls|biryani|kitchen|juice|cafe)",
    "groceries": r"(fruit|vegetable|dunzo|zepto|instamart|blinkit|bigbasket|bazar|bazaar|market|grocery|store|puja|pooja|mart|kirana|home need|mill|grofer|swiggystore|swiggyinstamart|hardcastle|milk)",
    "travel": r"(uber| ola|rapido|redbus|irctc|railway|flight|indian oil|uber|vogo|bykemania|petrol|\bhp|yatra|fuel|yeshakeerthi)",
    "online shopping": r"(amazon|flipkart|myntra|urbanic|razorpay|billdesktez|lenskart|mamaearth|ecomexpress|ekart|meesho|amzn)",
    "medical": r"(medicine|medical|hospital|doctor|pharma|pharmacy)",
    "styling": r"(salon|look|style|parlour|barber|glory a|beauty|fashion|cosmetic|dress|garment)",
    "recharge": r"(airtel|add money|postpaid|\bjio|stucred|communication|wallet|recharge|\bslice|mobikwik|kreditbee|krazybee|add-money|mpokket|\bsimpl|billdesk|pocketly)",
}
