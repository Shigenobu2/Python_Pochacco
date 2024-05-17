import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

start = args[1] #　駅名
goal = args[2]

dic = {"東京":0.00,"品川":6.78,"新横浜":25.54,
       "名古屋":342.02,"京都":476.31,"新大阪":515.35}

try:
    distance = abs(dic[start]-dic[goal])
    distance='{:.2f}'.format(distance)
    print(distance,end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")