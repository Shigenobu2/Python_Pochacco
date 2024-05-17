### 関数を使用して奇遇判定

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 関数の定義
def calcvalue(num):
    if num % 2 == 0:
        print(str(num) + "は偶数")
    else:
        print(str(num) + "は奇数")

# 引数の数だけ繰り返し処理
for i in args[1:]:
    # 関数の呼び出し
    calcvalue(int(i))