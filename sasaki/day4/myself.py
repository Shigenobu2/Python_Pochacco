# 引数渡しのモジュール
import sys
args = sys.argv

from introfamily import IntroFam

# Introクラスの作成
class Intro:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametxt = "私の名前は、" + self.name + "です。"
        return nametxt
    
    def age_out(self):
        agetxt = "年齢は、" + self.age + "です。"
        return agetxt

# インスタンス作成
test = IntroFam(args[1],args[2])

# メソッドの呼び出し
print(test.name_out())
print(test.age_out())