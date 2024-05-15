import sys
args = sys.argv

pop = int(args[1])
tuple = ("China","India","U.S.A","Indonesia","Pakistan","Brazil",
         "Nigeria","Bangladesh","Russia","Mexico")

print(tuple[pop-1],end="")

