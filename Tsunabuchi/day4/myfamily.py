import sys
from introfamily import IntroFam
args = sys.argv

outtext = IntroFam(args[1], args[2], args[3])


print(outtext.name_out())
print(outtext.age_out()) 
print(outtext.cat_out()) 