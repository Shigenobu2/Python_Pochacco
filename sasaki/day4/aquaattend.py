# 日付を扱うモジュールのインポート
import datetime

# 引数渡しのモジュール
import sys
args = sys.argv

# データベースを扱うモジュール
from database import session
from tables import Attendnum

# 文字列からオブジェクトに変換
date = datetime.datetime.strptime(args[1], "%Y%m%d")

info_data = {"entry_daye":date.date()}

# 登録するデータの編集
info_data = Attendnum(
    entry_date = date.date(),
    adult = args[2],
    child = args[3]
)