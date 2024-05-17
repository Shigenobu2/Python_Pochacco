from decimal import Decimal, ROUND_HALF_UP

def salary(suuzi):
    tax = 0 #　税
    income = 0 #　手取り

    if suuzi >= 1000000:
        tax = int((suuzi-1000000) * 0.2) + int(1000000 * 0.1)
    else:
        tax = int(suuzi * 0.1)

    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    income = suuzi - tax
    print("支給額:"+str(income)+"、税額:"+str(tax),end="")