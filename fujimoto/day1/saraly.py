import sys
args = sys.argv

saraly = int(args[1])

#100万円を超えるか
if (saraly<=1000000):
    tax = saraly * 0.1
    gave = saraly - tax

else:
    tax = 1000000*0.1 + (saraly- 1000000) * 0.2
    gave = saraly - tax

print("支給額:" +str(int(round(gave,1)))+ "、税額:" +str(int(round(tax,1))), end="")