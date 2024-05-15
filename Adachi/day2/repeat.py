import sys
args = sys.argv

suuzi = int(args[1])
plus = suuzi
while (plus<100):
    plus += suuzi
if plus == 100:
    print("Just 100!",end="")
else:
    print("Over!",end="")
print(plus)