from datetime import date
from database import session
from tables import Attendnum

import sys
args = sys.argv

# 登録するデータの編集
customer_counter= Attendnum(
    entry_date = date(args[1]),
    seq = 1
    adult = int(args[2])
    child = int(args[3])
)
session.add(customer_counter)
#コミット
session.commit()