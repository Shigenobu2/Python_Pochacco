import sys
args=sys.argv
num = int(args[1])
out=[]

for i in range(2,num+1) :
    if num%i==0:
        num=num/i
        out.append(i)
        if num%i==0:
            num=num/i
            out.append(i)

print(out)