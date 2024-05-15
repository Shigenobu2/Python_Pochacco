nationalities = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

import sys
args = sys.argv

index = int(args[1])

print(nationalities[index-1], end="")