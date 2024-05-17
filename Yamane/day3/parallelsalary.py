import sys
from func_salary import calcsalary
args=sys.argv
salary = int(args[1])
pay,tax=calcsalary(salary)
print("給与:"+str(salary)+"、"+"支給額:"+str(pay)+"、"+"税額:"+str(tax),end="")