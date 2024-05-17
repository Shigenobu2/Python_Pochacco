def calc_salary(salary):
    # 税金用の変数
    tax = 0.0

    # 税金の計算
    if salary>1000000:  # 100万円を超える部分の計算
        tax = ((salary-1000000)*0.2) + 100000
    else:               # 100万円以下の部分の計算
        tax = salary*0.1
    
    return salary-tax, tax