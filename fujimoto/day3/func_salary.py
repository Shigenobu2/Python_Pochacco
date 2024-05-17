import sys
args = sys.argv

def calcsalary(salary):
    #100万円を超えるか
    if (salary<=1000000):
        tax = salary * 0.1
        allowance = salary - tax
    else:
        tax = 1000000*0.1 + (salary- 1000000) * 0.2
        allowance = salary - tax

    allowance = int(round(allowance,1))
    tax = int(round(tax,1))

    return allowance, tax