import sys
args=sys.argv
num1=int(args[1])
num2=int(args[2])
num3=int(args[3])

def calcvalue(m,n,l):
    if m%2==0 :
        print(m+"は偶数")
    else :
        print(m+"は奇数")
    
    if n%2==0 :
        print(n+"は偶数")
    else :
        print(n+"は奇数")
    
    if l%2==0 :
        print(l+"は偶数")
    else :
        print(l+"は奇数")

calcvalue(num1,num2,num3)