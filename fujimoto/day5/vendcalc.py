coin = {10000:0, 5000:0, 1000:0, 500:0,100:0, 50:0, 10:0}
vending = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}
for key, value in vending.items():
    print(key + "：" + value + "円\n")

#投入金額入力
invest = int(input("投入金額を入力してください"))
'''
１．10000円を超える金額は購入できない
２．入力された金額では何も買えない（100円未満）
３．1円玉と5円玉は投入できない（10で割ると余りがでる）
'''
if invest <= 10000 and invest <= 100 and invest%10 != 0:
    #何を購入するか聞く
    which_buy =str(input("何を購入しますか（商品名/cansel）"))
    #選択したものが商品の中にある and 選択したものを買える投入金額である
    if which_buy in vending and invest >= int(vending[which_buy]):
        #所持金から購入分の金額を引く
        invest -= int(vending[which_buy])
        #まだ買えるものがある場合
        if invest <= 100:
            #残金表示
            print("残金：" +invest+ "円\n")
            #続けて購入するか尋ねる
            nextbuy = input("続けて購入しますか（Y/N）")
            #もうこないからね～
            if nextbuy == "N":
                print("おつり\n")
                for i in coin:
                    while invest != 0:
                        if invest-coin[0]>0:
                            invest -= coin[0]
                            coin[1] += 1
                        else:
                            print(coin[0] + "円玉：" + coin[1] + "枚\n")
                            break
            #お買い物をつづける
            elif nextbuy == "Y":


