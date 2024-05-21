import sys
from calcsum import SumCulc
args = sys.argv

three_input = SumCulc(args[1],args[2],args[3])

print(three_input.result())