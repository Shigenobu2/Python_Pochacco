import sys
from decimal import Decimal,ROUND_HALF_UP
args=sys.argv
salary = int(args[1])
if salary<=1000000 :
    tax=salary*0.1
    tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay=str(salary-tax)
    print("支給額:"+pay+"、"+"税額:"+str(tax))
else :
    tax=100000+(salary-1000000)*0.2
    tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    pay=str(salary-tax)
    print("支給額:"+pay+"、"+"税額:"+str(tax))

