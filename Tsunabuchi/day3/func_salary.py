import sys
args = sys.argv
payroll_amount = int(args[1]) #給与金額を入力


def calcsalary(payroll_amount):
   if (payroll_amount > 1000000):
      tax_amount = (int(payroll_amount) - 1000000) * 0.2 + 100000

   else:
      tax_amount = int(payroll_amount)  * 0.1

   pay_amount = int(payroll_amount) - int(tax_amount)

   print("支給額:" + str(round(pay_amount,1)) + "、税額:" + str(round(int(tax_amount),1)) ,end="")
