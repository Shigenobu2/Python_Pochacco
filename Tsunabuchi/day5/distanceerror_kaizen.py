import sys

# 引数の取得
args = sys.argv

# 引数を変数に代入
input_station1 = args[1]
input_station2 = args[2]

# 駅名と東京駅からの距離を辞書型に設定
stations = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

# のぞみ停車駅以外を入力した場合の例外処理
try:
   # 駅間の計算(絶対値)
   distance = abs(stations[input_station1] - stations[input_station2])
   # 出力（小数第二位まで）
   print(str(round(distance,2)),end="")
except:
   print("のぞみの停車駅を引数に設定してください")