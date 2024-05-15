### 指定された順位の国名を出力

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り int型
rank = int(args[1])

# 人口の順位リスト
rank_list = ["China", "India", "U.S.A", 
             "Indonesia", "Pakistan", "Brazil", 
             "Nigeria", "Bangladesh", "Russia", "Mexico"]

# 結果の表示
print(rank_list[rank-1], end="")