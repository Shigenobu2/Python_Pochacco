# 日付を扱うモジュールのインポート
import datetime

# 引数渡しのモジュール
import sys
args = sys.argv

# 文字列からオブジェクトに変換
date = datetime.datetime.strptime(args[1], "%Y%m%d")

# 曜日の取得
weekday = date.weekday()

# 出力用変数
result = 0

# 料金計算
if weekday <= 4:    # 平日の場合
    if int(args[2]) > 0:    # 大人がいる場合
        result += 2000 * int(args[2])
    if int(args[3]) > 0:  # 子供がいる場合
        result += 1200 * int(args[3])
else:               # 土日の場合
    if int(args[2]) > 0:    # 大人がいる場合
        result += 2400 * int(args[2])
    if int(args[3]) > 0:  # 子供がいる場合
        result += 1500 * int(args[3])

print(result, end="")