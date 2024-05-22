### 繰り返し構文を使用して、ひつじを数える

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り int型
num = int(args[1])

# 羊の数をカウントアップ
with open("Python_Pochacco/sasaki/day5/sheep.txt", mode="w", encoding="utf-8") as f:
    for i in range(1,num+1):    # 1からnum回繰り返す
        f.write("ひつじが" + str(i) + "匹\r\n")