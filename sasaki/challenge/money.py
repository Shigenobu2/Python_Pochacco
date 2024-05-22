class Money:
    def __init__(self, min_drink_price):
        self.min_drink_price = min_drink_price

    # おつりを返す関数
    def change_money(self, input_money):
        print("おつり")
        if input_money >= 5000:   # 5000札がある場合
            print("5000円札：1枚")  # 5000円札は多くて一枚
            input_money -= 5000
        if input_money >= 1000:   # 1000札がある場合
            # 何枚返すかをカウントする変数
            count = 0       
            while input_money >= 1000:
                count += 1
                input_money -= 1000
            print("1000円札：" + str(count) + "枚")
        if input_money >= 500:    # 500玉がある場合
            print("500円玉：1枚")  # 500円玉は多くて一枚
            input_money -= 500
        if input_money >= 100:    # 100玉がある場合
            # 何枚返すかをカウントする変数
            count = 0       
            while input_money >= 100:
                count += 1
                input_money -= 100
            print("100円玉：" + str(count) + "枚")
        if input_money >= 50:    # 50玉がある場合
            print("50円玉：1枚")  # 50円玉は多くて一枚
            input_money -= 50
        if input_money >= 10:    # 10玉がある場合
            # 何枚返すかをカウントする変数
            count = 0       
            while input_money >= 10:
                count += 1
                input_money -= 10
            print("10円玉：" + str(count) + "枚")

    # 入力がおかしくないかチェック
    def check_money(self, input_money):
        while True:
            if input_money >= 10000:    # 10,000円を超える金額が入力された場合
                print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
                input_money = int(input())
                continue
            elif input_money < self.min_drink_price:   # 購入できる商品がない場合（最低金額の商品より低い金額が入力された場合）
                print(str(input_money) + "円では購入できる商品がありません。再度投入金額を入力してください")
                input_money = int(input())
                continue
            elif str(input_money)[-1] != "0":   # 1円または5円が含まれている場合（1の位が0以外の場合）
                print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
                input_money = int(input())
                continue
            else:
                break

        
