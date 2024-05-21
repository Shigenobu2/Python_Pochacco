import sys
args = sys.argv

# 変数に代入
count = int(args[1])

# ファイルを開く
with open("files\sheep.txt", mode="a", encoding="utf-8") as f:
    for i in range(count):
        f.write("ひつじが"+ str(i + 1) + "匹\n")