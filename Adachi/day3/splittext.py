import sys
args = sys.argv

# 英文と何単語目を取り出すかの番号を入力
lan = args[1]
num = int(args[2])

# 単語を分割
res = lan.split()
print(res[num-1])