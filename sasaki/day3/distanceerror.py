### 辞書型で駅名と距離を定義、第二引数と第三引数の駅名の間の距離を算出

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

#四捨五入用のモジュール
from decimal import Decimal, ROUND_HALF_UP

# 引数の受け取り str型
station_1 = args[1]
station_2 = args[2]

# 駅名と距離の辞書を作成
dist_dict = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

# 引数で渡された駅同士の距離の算出
try:
    dist = dist_dict[station_1] - dist_dict[station_2]
except:
    print("のぞみの停車駅を引数に設定してください", end="")
    sys.exit()

#四捨五入(念のため)と絶対値表示
result = abs(Decimal(dist).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP))

# 結果の表示
print(result, end="")