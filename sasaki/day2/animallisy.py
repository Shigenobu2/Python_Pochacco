### 引数から受け取った動物のリストをいじる

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# リストの作成
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# 引数の受け取り
add_num = int(args[1])
add_animal = args[2]

# リストに追加
animals.insert(add_num, add_animal)

# リストの最後の要素の削除
del animals[-1]

# リストを昇順に並び替える
animals.sort()

# リストの表示
print(animals, end="")