import sys
from introduce import Intoro
args=sys.argv
a=Intoro(args[1],args[2])
print(a.name_out())
print(a.age_out())