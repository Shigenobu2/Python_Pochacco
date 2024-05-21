import sys
args = sys.argv

# 変数に代入
product = {"お茶":110,"コーヒー":100,
           "ソーダ":160,"コーンポタージュ":130}

print("お茶："+str(product["お茶"])+"円")
print("コーヒー："+str(product["コーヒー"])+"円")
print("ソーダ："+str(product["ソーダ"])+"円")
print("コーンポタージュ："+str(product["コーンポタージュ"])+"円")

# お金が正常に入力されたら２にする
money = 1

# お金入力
while(money !=2):
    credit = int(input("いくら払ってくれる？"))
    itien = str(credit)
    if credit < 100:
        print(f"{credit}円では購入できる商品はありません。再度投入金額を入力してください")
    elif credit > 10000:
        print("10000円を超える金額は投入できません。再度投入金額を入力してください")
    elif itien[len(itien)-1] != "0":
        print("１円玉、５円玉は使用できません。再度投入金額を入力してください")

    else:
        money = 2

# 購入フェーズ
while(credit >= 100):
    buy = input("何を購入しますか（商品名/cancel)")
    if credit < product[buy]:
        break

    credit -= product[buy]
    print(f"残金{credit}円")

    if input("続けて購入しますか(Y/N)") == "N":
        break


# おつり出力
print("おつり")
if int(credit/500) != 0:
    print("500円玉："+str(int(credit/500))+"枚")
if int((credit%500)/100) != 0:
    print("100円玉："+str(int((credit%500)/100))+"枚")
hyaku = int(credit%500)
if int((hyaku%100)/50) != 0:
    print("50円玉："+str(int((hyaku%100)/50))+"枚")
gozyu = int(hyaku%100)
if int((hyaku%50)/10) != 0:
    print("10円玉："+str(int((hyaku%50)/10))+"枚")

    



