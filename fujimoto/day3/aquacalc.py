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

if int(td.weekday()) == 5 or int(td.weekday()) == 6:
    adult_cost = adult*2400
    child_cost = child*1500
else:
    adult_cost = adult*2000
    child_cost = child*1200

m = adult_cost + child_cost

print(m, end="")