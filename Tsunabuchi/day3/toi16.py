import sys
args = sys.argv
day = int(args[1])
adult = int(args[2])
child = int(args[3])


import datetime

dt = datetime.datetime(int(day[0:4]), int(day[4:6]), int(day[6:8]))


if dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun" :
    adult_cost = 2400*adult
    child_cost = 1500*child
else:
    adult_cost = 2000*adult
    child_cost = 1200*child

m = adult_cost + child_cost

print(str(m), end="")