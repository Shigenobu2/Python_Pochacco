import sys
args = sys.argv

#四捨五入用のモジュール
from decimal import Decimal, ROUND_HALF_UP

salary = float(args[1])
tax = 0.0

if salary>1000000:
    tax = ((salary-1000000)*0.2) + 100000
else:
    tax = salary*0.1

print("支給額:" + str(Decimal(salary-tax).quantize(Decimal("0"),rounding=ROUND_HALF_UP)) 
      + "、税額:" + str(Decimal(tax).quantize(Decimal("0"),rounding=ROUND_HALF_UP)), end="")