from datetime import date
import sys
#mysqlDB接続、テーブル
from database import session
from tables import Holiday

args = sys.argv

input_date = args[1]
adult = int(args[2])
child = int(args[3])


dt = date(int(input_date[0:4]), int(input_date[4:6]), int(input_date[6:8]))


if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun" :
    pay = 2400 * adult + 1500 * child
#平日は、大人2,000円、子供1,200円
else:
    get_date = session.query(Holiday.holi_date).filter_by(holi_date = dt).first()
    if get_date is None:
        pay = 2000 * adult + 1200 * child  
    else:      
        pay = 2400 * adult + 1500 * child


print(pay, end="")