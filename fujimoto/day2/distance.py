distances = {'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}

import sys
args = sys.argv

start = str(args[1])
goal = str(args[2])

d = abs(distances[goal] - distances[start])

print(round(d,2), end="")