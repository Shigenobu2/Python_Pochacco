import sys
args = sys.argv
num = int(args[1])
animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animals.insert(num, animal)

animals.pop()

animals.sort()

print(animals,end="")