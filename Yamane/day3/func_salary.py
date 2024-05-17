def calcsalary (salary) :
    from decimal import Decimal,ROUND_HALF_UP
    if salary<=1000000 :
        tax=salary*0.1
        tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        pay=salary-tax
        
        
        
    else :
        tax=100000+(salary-1000000)*0.2
        tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        pay=salary-tax
    return pay,tax


        