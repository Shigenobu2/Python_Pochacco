import sys
args = sys.argv
station1 = args[1]
station2 = args[2]

distance = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

between = 0

try:
   between = abs(distance[station1] - distance[station2])
   print(str(round(between,2)),end="")
except:
   print("のぞみの停車駅を引数に設定してください")