import fanc_salary
import sys

args = sys.argv

for i in args[1:]:
    fanc_salary.salary(int(i))