import sys
from introduce import Intro
args = sys.argv

aiue = Intro(args[1], args[2])

print(aiue.name_out())
print(aiue.age_out())