### 引数から得られた文字列を空白区切りで単語に分け、指定された位置の単語を出力

# 引数渡しのモジュールのインポート
import sys
args = sys.argv

# 引数の受け取り str型、int型
sentence = args[1]
word_select_num = int(args[2])

# 英文を空白区切りで単語のリストに変換
word_list = sentence.split()

# 指定された位置の単語を抽出
word = word_list[word_select_num-1]

# 結果の表示
print(word, end="")
