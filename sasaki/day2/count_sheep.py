### 繰り返し構文を使用して、ひつじを数える

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り int型
num = int(args[1])

# 羊の数をカウントアップ
for i in range(1,num+1):    # 1からnum回繰り返す
    print("ひつじが" + str(i) + "匹")