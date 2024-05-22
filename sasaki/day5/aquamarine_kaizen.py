# モジュールのインポート
import datetime     # 日付 
import sys          # 引数受け渡し
args = sys.argv

# 料金計算関数
def calc_fee(weekday_num):
    calc_result = 0
    if weekday_num == 5 & weekday_num == 6:    # 土日の場合
        calc_result = (2400 * int(args[2])) + (1500 * int(args[3]))
    else:                              # 平日の場合
        calc_result = (2000 * int(args[2])) + (1200 * int(args[3]))
    return calc_result

# 文字列からオブジェクトに変換
date = datetime.datetime.strptime(args[1], "%Y%m%d")

# 曜日の取得
weekday = date.weekday()

# 料金計算関数の呼び出し
result = calc_fee(weekday)

# 結果の出力
print(result, end="")