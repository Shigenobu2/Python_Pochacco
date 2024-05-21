import sys
args = sys.argv

#　新幹線の駅間を計算する

# 東京を起点としてそれぞれの駅を辞書型で管理
dic = {"東京":0.00,"品川":6.78,"新横浜":25.54,
        "名古屋":342.02,"京都":476.31,"新大阪":515.35}

# str型変数定義
start = ""
goal = ""

#　エラー対応
try:
# 駅名を変数に格納（1:スタート,2:ゴール）
    start = args[1]
    goal = args[2]

    #　２駅間の差分を求める
    distance = abs(dic[start]-dic[goal])
    #　少数第２位まで出力
    distance='{:.2f}'.format(distance)
    print(distance,end="")


except KeyError:
    print("駅名が異なります。正しい駅名を出力してください。",end="")

except IndexError:
    print("引数が不足しています。駅名を２つ出力してください。",end="")

except:
    print("想定外のエラーです。正しく駅名を入力してください。")
