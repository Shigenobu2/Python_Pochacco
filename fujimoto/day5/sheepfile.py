import sys
args = sys.argv

sheep = int(args[1])

sheeptxt = open("projects/Python_Pochacco/fujimoto/day5/sheep.txt", mode="w", encoding="utf-8")

for i in range(1, sheep+1):
    sheeptxt.write("ひつじが" + str(i) + "匹\n")

sheeptxt.close()