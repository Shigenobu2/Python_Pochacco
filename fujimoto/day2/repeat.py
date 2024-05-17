import sys
args = sys.argv

plus = int(args[1])
sum= 0

while True:
    sum += plus
    if sum == 100:
        print("Just 100!", end="")
        break
    elif sum > 100:
        print("Over!", end="")
        break