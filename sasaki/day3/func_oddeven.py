### 関数を使用して奇遇判定

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り リスト
input = args[1:]

# 関数の定義
def calcvalue(num):
    if num % 2 == 0:
        print(str(num) + "は偶数", end="")
    else:
        print(str(num) + "は奇数", end="")

# 引数の数だけ繰り返し処理
for i in input:
    # 関数の呼び出し
    num = int(input[i])
    calcvalue(num)