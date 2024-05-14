import sys
args = sys.argv

salary = float(args[1])
tax = 0.0

if salary>1000000:
    tax = ((salary-1000000)*0.2) + 100000
else:
    tax = salary*0.1

print("支給額:" + str(round(salary)-round(tax)) + "、税額:" + str(round(tax)), end="")