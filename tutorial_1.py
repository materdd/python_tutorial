###### Pythonの基礎 #####
# GOAL: Pythonの基礎的な実装ができる
# pythonの標準変数：文字列、数値、リスト、タプル、辞書、条件分岐（if）、繰り返し（for, while）
# 


#----- 文字列 -----#
# %% 
#プログラミング言語入門でおなじみの「Hello, world!」の出力

print("Hello, world!")

# %% 以下のセルは、四則演算。
print(1 + 1)
print(2 - 1)
print(2 * 5)
print(6 / 2)
print(10 ** 3) # 10の3乗, 〜乗は**を使う
print(10 % 3) # 余り

# %% 文字列(double quotation or single quotation)
# 変数（sample_str）に文字列を割り当てる
sample_str = "hello world"
print(sample_str)
sample_str = 'hello world'
print(sample_str)
sample_str = 'hello"aaa"world'
print(sample_str)
sample_str = "hello'aaa'world"
print(sample_str)

"""
double quotationとsingle quotationは、文法上差異は無いが、
可読性を上げるため、チームでそろえるべき。
英語キーボードだとsinglのほうが打ちやすく、日本語キーボードだと、
doubleのほうが打ちやすい
"""

# %% 文字の抜き出しも可能。なお、0から始まる。
sample_str[0]

# %% 2番目の文字は1を指定
sample_str[1]

# %% 最後の文字は-1を指定
sample_str[-1]

# %% 存在しないインデックスを指定しても実行してもエラーが出るので注意
sample_str[20]



### 数値 ###
# %%
sample_data_int = 1
print(sample_data_int)

# 上の数字に10を足す
sample_data_int = sample_data_int + 10
print(sample_data_int)

# 同じ変数に結果を格納する場合は、下記の通り記載も可能
sample_data_int += 10
print(sample_data_int)
sample_data_int *= 10
print(sample_data_int)

"""
通常、他のプログラミング言語では、int（整数）、float（少数）の型の割り当てを
下記の通り変数名の前に指定する。
int a = 1
float b = 3.4

pythonでは、型の割り当ては自動で行われる。
"""
"""
変数に絶対的な命名規則は無いですが、自分または第三者が見て
分かりやすい変数名を付けましょう。（下記参考サイト）
https://pep8-ja.readthedocs.io/ja/latest/
"""
"""
他、変数に関する注意点として、プログラミング言語には、予約語といわれる、
あらかじめ用意してある変数や組み込みオブジェクトなど(while, if, sumなど)
がありますので、それらを変数名として使わないように注意しましょう。
"""


#----- List -----#
# %%
sample_data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sample_data_list)

# typeで変数のタイプがわかる
print("変数のタイプ:", type(sample_data_list))

# 1つの要素を指定。0から始まり、[1]は2番目になるので注意。
print("2番目の数：", sample_data_list[1])

# typeで変数のタイプがわかる
print("変数のタイプ:", type(sample_data_list[1]))

# lenで要素の数を出力。ここでは1から10までの10個なので、結果は10。
print("要素数：", len(sample_data_list))

sample_data_list_2 = sample_data_list * 2
print(sample_data_list_2)


#--- tuple ---#
# %%
"""
tupleはlistとほぼ同じなのだが、要素の書き換えが不可能。
そのため、値を変えてほしくない場合等に使うが、
使う頻度は少ない
"""
sample_data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("変数のタイプ:", type(sample_data_tuple))

# 1つの要素を指定。0から始まり、[1]は2番目になるので注意。
print("2番目の数：", sample_data_tuple[1])

# typeで変数のタイプがわかる
print("変数のタイプ:", type(sample_data_tuple[1]))


# %%
sample_data_tuple[0] = 100
print(sample_data_tuple)

#----- 辞書 -----#
# %%
sample_dic_data = {'apple': 100, 'banana': 100, 'orange': 300, 'mango': 400, 'melon': 500}
print(sample_dic_data['melon'])

"""
キー（melon, orange等）を指定して、バリュー（100,300）を取り出す。
"""


#----- if（条件分岐） -----#
# %% 例１
a = 1

if a == 1:
    print("a = 1")
elif a == 2:
    print("a = 2")
elif (a >= 3) & (a < 100):
    print("aは3以上かつ100未満")
else:
    print("それ以外")

# %% 例2
sample_int = 5
sample_data_list = [0,1,2,3,4,5,6,7]

if sample_int in sample_data_list:
    #　" " の中に、扱っている変数を表示させたい場合は、以下のように %dと%を組み合わせる
    print("%d は入っています。" % (sample_int))
else:
    print("%d は入っていません。" % (sample_int))

"""
%d は整数、%s は文字列、%f は浮動小数点数の場合に設定します。
文字列フォーマットといいます。
他、「print("{} は入っていません。".format(sample_int))」
のようにして表示することも可能です（変数を複数設定することもできます）。
このformat記法はPython2.6から登場した方法で、%記法を拡張したものとなります。
%記法は今後廃止される可能性があるため注意が必要です。
"""



#----- for（繰り返し処理） -----#
# %% 例1
# 初期値の設定
total_num = 0

# for 文
for num in [0, 1, 2]:
    # 取り出した数の表示
    print("num:", num)
    # 今まで取り出した数の合計
    total_num = total_num + num

# 最後に合計を表示
print("total_num:", total_num)

# %% 例2（range関数）
# 初期値の設定
total_num = 0

# for 文
for num in range(0,3):
    # 取り出した数の表示
    print("num:", num)
    # 今まで取り出した数の合計
    total_num = total_num + num

# 最後に合計を表示
print("total_num:", total_num)

# %% 例3（range関数、skip）
# 初期値の設定
total_num = 0

# for 文
for num in range(0,10,2):
    # 取り出した数の表示
    print("num:", num)
    # 今まで取り出した数の合計
    total_num = total_num + num

# 最後に合計を表示
print("total_num:", total_num)

# %% 例4（辞書）
sample_dic_data = {'apple': 100, 'banana': 100, 'orange': 300, 'mango': 400, 'melon': 500}
for dic_key in sample_dic_data:
    print(dic_key, sample_dic_data[dic_key])

# %% 例5（複数変数処理）
for one, two in zip([1, 2, 3], [11, 12, 13]):
    print("", one, "&", two)



#----- while -----#
# %%
sample_int = 1 
while sample_int <= 10:
    print(sample_int)
    sample_int = sample_int + 1

print(sample_int)



# %%
