# ファイルを開く
a_file = open("sheep.txt", mode="a", encoding="utf-8")

# ファイルに書き込む

import sys
args = sys.argv
num = int(args[1])

for n in range(1, num + 1):
    a_file.write("ひつじが" + str(n) + "匹\n")

a_file.close()