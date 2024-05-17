import sys
args = sys.argv
text = args[1]
num = int(args[2])


s = text.split()

print(s[num-1],end="")

