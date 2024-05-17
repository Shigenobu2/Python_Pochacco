import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
if hm_class == "果物類":    # 果物類の場合
    for i in fruits:
        hinmoku[i] -= price_down
        if hinmoku[i] <= 0:  # 例外処理　0円以下になる場合は1円にする
            hinmoku[i] = 1
elif hm_class == "酒類":    # 酒類の場合
    for i in alcohol:
        hinmoku[i] -= price_down
        if hinmoku[i] <= 0:  # 例外処理　0円以下になる場合は1円にする
            hinmoku[i] = 1
elif hm_class == "麺類":    # 麺類の場合
    for i in noodles:
        hinmoku[i] -= price_down
        if hinmoku[i] <= 0:  # 例外処理　0円以下になる場合は1円にする
            hinmoku[i] = 1

print(hinmoku, end="")