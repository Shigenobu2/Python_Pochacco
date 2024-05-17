import sys
args=sys.argv
text=args[1]
num=int(args[2])
text=text.split()
print(text[num-1],end="")

