# モジュールのインポート
import sys

# 例外処理用に最低金額のドリンクの値段を算出する関数
def calc_min_price(drink_dict):
    min_price = 0
    for i in drink_dict:
        if min_price == 0:      # 最初だけ最小値に設定
            min_price = drink_dict[i]
            continue   
        if min_price > drink_dict[i]:   # 最小値を比較
            min_price = drink_dict[i]
    return min_price

# おつりを返す関数
def change(money):
    print("おつり")
    if money >= 5000:   # 5000札がある場合
        print("5000円札：1枚")  # 今回は自販機で5000円札は多くて一枚なのでそのまま出力
        money -= 5000
    if money >= 1000:   # 1000札がある場合
        # 何枚返すかをカウントする変数
        count = 0       
        while money >= 1000:
            count += 1
            money -= 1000
        print("1000円札：" + str(count) + "枚")
    if money >= 500:    # 500玉がある場合
        print("500円玉：1枚")  # 500円玉は多くて一枚なのでそのまま出力
        money -= 500
    if money >= 100:    # 100玉がある場合
        # 何枚返すかをカウントする変数
        count = 0       
        while money >= 100:
            count += 1
            money -= 100
        print("100円玉：" + str(count) + "枚")
    if money >= 50:    # 50玉がある場合
        print("50円玉：1枚")  # 50円玉は多くて一枚なのでそのまま出力
        money -= 50
    if money >= 10:    # 10玉がある場合
        # 何枚返すかをカウントする変数
        count = 0       
        while money >= 10:
            count += 1
            money -= 10
        print("10円玉：" + str(count) + "枚")


# ドリンクのリスト
drinks = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

# 最低価格の商品の金額
min_drink = calc_min_price(drinks)

# 購入できる商品の表示
for i in drinks:
    print(i + "：" + str(drinks[i]))

# 何円入れたか　ユーザー入力待ち
print("投入金額を入力してください")
input_money = int(input())

# 例外処理
while True:
    if input_money >= 10000:    # 10,000円を超える金額が入力された場合
        print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        input_money = int(input())
        continue
    elif input_money < min_drink:   # 購入できる商品がない場合（最低金額の商品より低い金額が入力された場合）
        print(str(input_money) + "円では購入できる商品がありません。再度投入金額を入力してください")
        input_money = int(input())
        continue
    elif str(input_money)[-1] != "0":   # 1円または5円が含まれている場合（1の位が0以外の場合）
        print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
        input_money = int(input())
        continue
    else:
        break

# 商品購入を繰り返す
while True:
    # 何を購入したいか　ユーザー入力待ち
    print("何を購入しますか（商品名/cancel）")
    input_name = input()

    # cancelと打たれたらお金を返して終了
    if input_name == "cancel":
        change(input_money)
        sys.exit()

    # 商品の購入処理
    try:
        # 投入金額を更新
        input_money -= drinks[input_name]    

        # 購入後に最低価格の飲み物の金額を下回っていた場合　お釣りを出して終了
        if input_money < min_drink:
            change(input_money)
            sys.exit()

        # 残金の表示
        print("残金：" + str(input_money) + "円")
        while True:
            # 購入を続けるか選択（ユーザー入力）
            print("続けて購入しますか（Y/N）")
            next_buy = input()
            if next_buy == "Y":      # 続けて購入する場合
                # 購入できる商品の表示
                for i in drinks:
                    print(i + "：" + str(drinks[i]))
                break
            elif next_buy == "N":    # 購入をやめる場合
                # お釣りの金額を出力して終了
                change(input_money)
                sys.exit()
            else:                   # Y/N以外が入力された場合
                print("エラー：有効な文字を入力してください。")
                continue
    except KeyError:     # 例外処理　入力された商品名がリストにない場合
        print("リストにある商品名を入力してください")
        continue

            

        






# 購入後の残金で最低価格の飲み物が買えるかどうか
if input_money - drinks[input_name] < min_drink:    # 購入後の残金が最低金額の飲み物の価格を下回っていた場合
    change(input_money)