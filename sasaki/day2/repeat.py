# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り int型
num = int(args[1])

# 合計値を格納する変数の初期化
sum = num

# 無限足し算
while sum < 100:
    sum += num
    if sum == 100:    # ちょうど100になった場合
        print("Just 100!", end="")
        break
    elif sum > 100:   # 100を超えた場合
        print("Over!", end="")
        break