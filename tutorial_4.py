###### Pythonの基礎 #####
# GOAL: Numpy、Scipy、Pandas、Matplotlibのモジュールを
# 読み込みそれらの基本的な役割を知る


""" 便利モジュール（関数群）
Numpy: 多次元配列処理
Pandas: 表計算やデータベースのようなデータ操作
Matplotlib: データ可視化（プロット）
"""

#----- numpy -----#
# %% numpy module import
"""
多次元配列を処理することができます。
実際に扱うデータは多次元であることが多く、
その処理をするためにNumpyを使うと便利です。
また、NumpyはCで実装されており、処理が高速です。
"""

# numpyモジュールの読み込み
import numpy as np

# %% initialize
sample_numpy_data = np.array([9,2,3,4,10,6,7,8,1,5])
print(sample_numpy_data)

# %% list -> numpy
temp = [0,1,2,3,565,3]
temp = np.array(temp)
print(type(temp))

# %%　
# 型の表示
print("型の表示", sample_numpy_data.dtype)

# 次元数
print("次元数:", sample_numpy_data.ndim)

# 要素数
print("要素数:", sample_numpy_data.size)

# %%
# それぞれの要素同士での演算
print("掛け算:",np.array([1,2,3,4,5,6,7,8,9,10]) * np.array([10,9,8,7,6,5,4,3,2,1]))
print("累乗:",np.array([1,2,3,4,5,6,7,8,9,10]) **2)
print("割り算:",np.array([1,2,3,4,5,6,7,8,9,10]) / np.array([10,9,8,7,6,5,4,3,2,1]))

# %%
# 0や1の初期化データ
# (2,3)は2行3列の行列データを作っています。
zero_data = np.zeros((2,3), dtype=np.int32)
one_data = np.ones((2,3), dtype=np.float32)

print("0でint型 \n", zero_data)

print("1でfloat型 \n", one_data)


# %%
# 値が大きい順に並び替える
print("そのまま：",sample_numpy_data)

# sorting
sample_numpy_data.sort()
print("ソート後：",sample_numpy_data)

# 最小値
print("Min:",sample_numpy_data.min())

# 最大値
print("Max:",sample_numpy_data.max())

# 合計
print("Sum:",sample_numpy_data.sum())

# %%
# データ準備
sample_multi_array_data = np.arange(9)
print("initialize: \n", sample_multi_array_data)
sample_multi_array_data = sample_multi_array_data.reshape(3,3)
print("reshape: \n", sample_multi_array_data)

# 行の抜き出し
print("行の抜き出し: \n", sample_multi_array_data[0,:])

# 列の抜き出し
print("列の抜き出し: \n", sample_multi_array_data[:,0])




#----- pandas -----#
# %%
"""
Pandasを使うと、データの様々なハンドリングをスムーズに柔軟に実施することができ、
表計算や後ほど学ぶデータベースのようなデータ操作が可能となります。
"""

# import
from pandas import Series,DataFrame
import pandas as pd

# %%
# series(配列のようなオブジェクト)
sample_pandas_data = pd.Series([10,11,12,13,14,15,16,17,18,19])
print(sample_pandas_data)

# プロパティを表示
print("データの値:",sample_pandas_data.values)
print("インデックスの値:",sample_pandas_data.index)

# %% インデックスのラベル指定
sample_pandas_index_data = pd.Series([10,11,12,13,14,15,16,17,18,19]
                                     ,index=['a','b','c','d','e','f','g','h','i','j'])
print(sample_pandas_index_data)
print("データの値:",sample_pandas_index_data.values)
print("インデックスの値:",sample_pandas_index_data.index)


# %% DataFrame（各々の列で異なる型を持たせることが可能）
attri_data1 = {'ID':['100','101','102','103','104']
        ,'city':['Tokyo','Osaka','Kyoto','Hokkaidao','Tokyo']
        ,'birth_year':[1990,1989,1992,1997,1982]
        ,'name':['Hiroshi','Akiko','Yuki','Satoru','Steeve']}

attri_data_frame1 = DataFrame(attri_data1)

print(attri_data_frame1)

# %%
# 列の抜き取り（一つ）
print(attri_data_frame1.birth_year)

# 列の抜き取り（複数）
attri_data_frame1[["ID","birth_year"]]

# %%
# 条件（フィルター）
attri_data_frame1[attri_data_frame1['city']=='Tokyo']

# 条件（フィルター、複数の値）
attri_data_frame1[attri_data_frame1['city'].isin(['Tokyo','Osaka'])]

# %% データの列の削除
attri_data_frame1.drop(['birth_year'],axis=1)

"""
その他、Dataframe同士の統合、ソーティング等の様々な機能が存在。
excelと同じような利便性で利用可能
"""

# %% excel dataの読み込み
df = pd.read_excel("data/tutorial_4_1.xlsx")
print(df)

# %% excelに保存
attri_data_frame1.to_excel("data/tutorial_4_pandas_to_excel.xlsx", sheet_name="test")



#----- matplotlib -----#
# %%
"""
データを可視化する
https://matplotlib.org/
"""
# import
# matplotlib と seabornの読み込み
# seabornはきれいに図示できる
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# ここで表示させるために必要なマジックコマンド
%matplotlib inline

# %% 散布図
import numpy.random as random

#　シード値の固定
random.seed(0)
# x軸のデータ
x = np.random.randn(30)
# y軸のデータ
y = np.sin(x) + np.random.randn(30)

# plot
plt.plot(x, y, "o")

#以下でも散布図が描ける
#plt.scatter(x, y)

# title
plt.title("Title Name")
# Xの座標名
plt.xlabel("X")
# Yの座標名
plt.ylabel("Y")

# gridの表示
plt.grid(True)


# %% 連続曲線
np.random.seed(0)
# データの範囲
numpy_data_x = np.arange(1000)

# 乱数の発生と積み上げ
numpy_random_data_y = np.random.randn(1000)

# label=とlegendでラベルをつけることが可能
plt.plot(numpy_data_x,numpy_random_data_y,label="Label")
plt.legend()

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)


# %% sin関数

# 2行1列のグラフの1つ目
plt.subplot(2,1,1)
x = np.linspace(-10, 10, 100)
plt.plot(x, np.sin(x)) 

# 2行1列のグラフの2つ目
plt.subplot(2,1,2)
y = np.linspace(-10, 10, 100)
plt.plot(y, np.sin(2*y)) 

plt.grid(True)

