import sys
args=sys.argv
category=args[1]
price_down=int(args[2])
price_table={"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}
if category=="麺類" :
    price_table["ラーメン","うどん","パスタ"]-=price_down
    print(price_table,end="")

if category=="酒類名" :
    price_table["ビール","日本酒"]-=price_down
    print(price_table,end="")

if category=="果物類" :
    price_table["リンゴ","みかん","バナナ"]-=price_down
    print(price_table,end="")
       