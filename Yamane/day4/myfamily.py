import sys
from introfamily import IntroFam 
args=sys.argv
a=IntroFam(args[1],args[2],args[3])
print(a.name_out())
print(a.age_out())
print(a.cat_out())