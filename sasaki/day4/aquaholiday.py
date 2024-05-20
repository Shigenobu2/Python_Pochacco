# 日付を扱うモジュールのインポート
import datetime

# 引数渡しのモジュール
import sys
args = sys.argv

# データベースを扱うモジュール
from database import session
from tables import Holiday

# 文字列からオブジェクトに変換
date = datetime.datetime.strptime(args[1], "%Y%m%d")

# 曜日の取得
weekday = date.weekday()

# データを取得する
holidaylist=session.query(Holiday).all()

# 出力用変数
result = 0

# 料金計算
if weekday == 5 & weekday == 6:     # 土日の場合
    print("入力された日付は土日です")
    result += 2400 * int(args[2]) + 1500 * int(args[3])
else:   # 平日の場合
    for holiday in holidaylist:
        if date.date() == holiday.holi_date:    # 平日の中でも祝日の場合
            print("入力された日付は祝日です:", holiday.holi_text)
            result += 2400 * int(args[2]) + 1500 * int(args[3])
            break
    else:
        print("入力された日付は平日です")
        result += 2000 * int(args[2]) + 1200 * int(args[3])

print(result, end="")


