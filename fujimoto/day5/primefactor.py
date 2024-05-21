import sys
args = sys.argv

num = int(args[1])

i = 2
pf = []

while num != 1:
    if num%i ==0:
        pf.append(i)
        num/=i
    else:
        i+=1

print(pf, end="")