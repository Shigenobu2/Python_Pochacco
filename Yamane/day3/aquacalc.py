import sys
from datetime import datetime

# コマンドライン引数を取得
args = sys.argv
date = args[1]  # 文字列として受け取る
adult_num = int(args[2])
children_num = int(args[3])

# 文字列から日付オブジェクトを作成
date_object = datetime.strptime(date, "%Y%m%d")  # 正しいフォーマット指定子を使用
day_of_week = date_object.weekday()

# 平日の価格計算関数
def workday(a, b):
    return a * 2000 + b * 1200

# 休日の価格計算関数
def holiday(c, d):
    return c * 2400 + d * 1500

# 曜日に応じて価格を計算して出力
if day_of_week < 5:
    print(workday(adult_num, children_num), end="")
else:
    print(holiday(adult_num, children_num), end="")

