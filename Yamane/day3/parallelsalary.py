import sys #引数を設定するためにsysをインポート
from func_salary import calcsalary #func_salaryから税金と支払い額を求める関数calcsalaryをインポート

#引数で受け取った給与を変数salaryに代入
args=sys.argv
salary = int(args[1])

#変数pay,taxに関数calcsalaryで求めた支払い額と税金を代入
pay,tax=calcsalary(salary)
#給与、支払い額、税額を出力
print("給与:"+str(salary)+"支給額:"+str(pay)+"税額:"+str(tax))