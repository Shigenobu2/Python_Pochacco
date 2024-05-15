import sys
args=sys.argv
input=int(args[1])
animal=args[2]
animals=[ "giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(input,animal)
del animals[5]
animals.sort()
print(animals,end="")
