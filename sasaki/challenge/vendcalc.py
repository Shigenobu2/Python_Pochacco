# モジュールのインポート
import sys
from money import Money

# 最低金額のドリンクの値段を算出する関数
def calc_min_price(drink_dict):
    min_price = 0
    for i in drink_dict:
        if min_price == 0:      # 最初だけ最小値に設定
            min_price = drink_dict[i]
            continue   
        if min_price > drink_dict[i]:   # 最小値を比較
            min_price = drink_dict[i]
    return min_price


# ドリンクのリスト
drinks = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

# 最低価格の商品の金額
min_drink_price = calc_min_price(drinks)

# 購入できる商品の表示
for i in drinks:
    print(i + "：" + str(drinks[i]))

# 何円入れたか　ユーザー入力待ち
print("投入金額を入力してください")
input_money = int(input())

# インスタンス作成
vend_money = Money(min_drink_price)

# 投入金額に誤りはないかをチェック
input_money = vend_money.check_money(input_money)



# 商品購入を繰り返す
while True:
    # 何を購入したいか　ユーザー入力待ち
    print("何を購入しますか（商品名/cancel）")
    input_name = input()

    # cancelと打たれたらお金を返して終了
    if input_name == "cancel":
        vend_money.change_money(input_money)
        sys.exit()

    # 商品の購入処理
    try:
        # 投入金額を更新
        input_money -= drinks[input_name]    

        # 購入後に最低価格の飲み物の金額を下回っていた場合　お釣りを出して終了
        if input_money < min_drink_price:
            vend_money.change_money(input_money)
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
                vend_money.change_money(input_money)
                sys.exit()
            else:                   # Y/N以外が入力された場合
                print("エラー：有効な文字を入力してください。")
                continue
    except KeyError:     # 例外処理　入力された商品名がリストにない場合
        print("リストにある商品名を入力してください")
        continue
