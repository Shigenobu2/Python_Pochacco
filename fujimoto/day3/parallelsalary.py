import sys
import func_salary

args = sys.argv

allowance,tax = func_salary.calcsalary(int(args[1]))

print("給与:" +str(args[1])+ "、支給額:" +str(allowance)+ "、税額:" +str(tax), end="")