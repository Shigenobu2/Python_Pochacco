#税金と支払い額を求める関数calcsalary
def calcsalary (salary) :
    from decimal import Decimal,ROUND_HALF_UP
    #給与が100万円以下の場合    
    if salary<=1000000 :
        tax=salary*0.1 #税金の計算
        tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) #税金の値を小数点第一位で四捨五入
        pay=salary-tax #支払い額の計算
        
        
    #給与が100万円以上の場合    
    else :
        tax=100000+(salary-1000000)*0.2 
        tax=Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) 
        pay=salary-tax
        
    #支払い額と税金の値を返す    
    return pay,tax


        