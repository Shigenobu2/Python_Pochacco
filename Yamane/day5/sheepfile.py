import sys
args=sys.argv
sheep_count=int(args[1])

with open ("C:\Seminar\python\\files\sheep.txt",mode="w",encoding="utf-8") as f:
    for i in range(sheep_count):
        f.write("ひつじが"+ str(i+1) + "匹")