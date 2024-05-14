import sys
args = sys.argv

suuzi = int(args[1])

if suuzi % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")