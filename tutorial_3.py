###### Pythonの基礎 #####
# GOAL: クラス、インスタンス

# https://www.atmarkit.co.jp/ait/articles/0803/12/news148.html

"""
pythonはオブジェクト指向型のプログラミング言語す。
クラスは「オブジェクトのひな型」みたいなものです。
よく例えられる例が「たい焼き」で、以下のclassのPrintClass
はたい焼き機の型を作っています。
次に、実際のたい焼きが出来上がったのがインスタンスp1というイメージです。
インスタンスとは、クラスからできあがる実体です。
インスタンスには属性を追加することができ、
以下ではp1.xに10、p1.yに100、p1.zに1000を追加しています。
以下はクラスとインスタンスのイメージです。
"""

# %% 例1
class Taiyaki(object): # 通常は先頭文字は大文字
    def __init__(self, price, num): # 初期化
        self.price = price
        self.num = num

    def calc_price(self):
        return self.price * self.num

taiyaki_anko = Taiyaki(100, 3)
print("taiyaki anko:", taiyaki_anko.calc_price())
taiyaki_cream = Taiyaki(120, 5)
print("taiyaki cream:", taiyaki_cream.calc_price())

# %% 例2
class MyCalcClass:
    def __init__(self, x, y): #初期化
        self.x = x
        self.y = y
        
    def calc_add1(self, a, b):
        return a + b
    
    def calc_add2(self):
        return self.x + self.y

    def calc_mutli(self, a, b):
        return a * b

    def calc_print(self, a):
        print("data:", a, "&", self.y)

instance_1 = MyCalcClass(1, 2)
instance_2 = MyCalcClass(5, 10)

print("2つの数の足し算(新たに数字を引数としてセット):", instance_1.calc_add1(5, 3))
print("2つの数の足し算(インスタンス化の時の値):", instance_1.calc_add2())
print("2つの数のかけ算:", instance_1.calc_mutli(5, 3))
instance_1.calc_print(5)
