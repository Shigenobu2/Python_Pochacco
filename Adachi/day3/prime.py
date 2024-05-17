import sys
args = sys.argv

def prime_fact(n):
    fact = []
    # 2のときのみ
    while n % 2 == 0:
        fact.append(2)
        n //= 2
    # 3以上ただし、素数であるかないかを分ける
    f = 3
    while f * f <= n:
        if n % f == 0:
            fact.append(f)
            # 整数を返す
            n //= f
        else:
            f += 2
    if n != 1:
        fact.append(n)
    return fact

#引数を変数に代入
num = int(args[1])    
print(prime_fact(num),end="")
