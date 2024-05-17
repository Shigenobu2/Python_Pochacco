import sys
from decimal import Decimal, ROUND_HALF_UP
import datetime as dt

args = sys.argv

day = args[1] #　日にち
ada = int(args[2]) # 大人の人数
kid = int(args[3])# 子供の人数

# 平日料金
hei = [2000,1200]

# 休日料金
donit = [2400,1500]
date = dt.date(int(day[0:4]),int(day[4:6]),int(day[6:8]))

sum = 0
print(date.strftime('%A'))
# 平日か土日か判断
if date.strftime('%A') == "Saturday" or date.strftime('%A') == "Sunday":
    sum = donit[0]*ada + donit[1]*kid
else:
    sum = hei[0]*ada + hei[1]*kid

print(sum,end = "")