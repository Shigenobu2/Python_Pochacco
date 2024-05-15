import sys
args = sys.argv

text = str(args[1])
num = int(args[2])

words = text.split()

print(words[num-1])