import sys
args = sys.argv

math = args[1]
ja = args[2]
en = args[3]

#1. 3教科とも70点以上、または、合計点数が220点以上
sum = int(math) + int(ja) + int(en)

if (int(math) >= 70) and (int(ja) >= 70) and (int(en) >= 70):
    judge = "合格"
else:
    judge = "不合格"

#2. 1科目も50点未満がない
if (sum >= 220) and (int(math) >= 50) and (int(ja) >= 50) and (int(en) >= 50):
    judge = "合格"

print(judge, end="")