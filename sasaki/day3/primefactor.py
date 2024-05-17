# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り int型
num = int(args[1])

# カウントアップ変数
n = 2

# 出力する配列の初期化
result = []

# 割った結果が1になるまで繰り返し
while num != 1:
    # 割った余りが0の時は入力値の因数である
    if num%n == 0:
        # 出力配列に追加
        result.append(int(n))
        # 元の数値を割った値に変更
        num /= n
        # カウントアップ変数のリセット
        n = 2
        continue

    # カウントアップ変数をカウントアップ
    n += 1

print(result, end="")