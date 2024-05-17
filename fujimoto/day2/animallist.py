animal = ["giraffe", "tiger", "zebra", "elephant", "lion"]

import sys
args = sys.argv

index = int(args[1])
ani = str(args[2])

animal.insert(index, ani)

animal.pop()
animal.sort()

print(animal, end="")