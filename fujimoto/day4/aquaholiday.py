from database import session
from tables import Holiday

import datetime
import sys
args = sys.argv

today = args[1]
y = int(today[0:4])
m = int(today[4:6])
d = int(today[6:8])

td = datetime.date(y,m,d)
adult = int(args[2])
child = int(args[3])

# データを取得する
holidaylist=session.query(Holiday.holi_date).filter_by(holi_date=td).first()
print(td)
print(holidaylist)

if int(td.weekday()) == 5 or int(td.weekday()) == 6 or holidaylist!=None:
    adult_cost = adult*2400
    child_cost = child*1500
else:
    adult_cost = adult*2000
    child_cost = child*1200

m = adult_cost + child_cost

print(m, end="")