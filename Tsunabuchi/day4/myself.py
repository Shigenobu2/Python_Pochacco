import sys
from introduce import Intro
args = sys.argv


outtext = Intro(args[1], args[2])


print(outtext.name_out()) #名前の出力
print(outtext.age_out())  #年齢の出力