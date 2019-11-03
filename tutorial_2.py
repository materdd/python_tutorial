###### Pythonの基礎 #####
# GOAL: 関数の習得

# %% 例1
"""
defを使って、関数を作成しています。
関数を作成すると、同じような処理を実行したいときに、便利です。
また、処理をまとめておくと、後でコードを修正するときも便利です。
1つ目のcalc_multi関数は、2つの数字（aとb）を引数として、
その掛け算を返しています。
この引数がインプットとなって、returnで結果を返し（返り値といいます）、
これがアウトプットになります。
その次の関数calc_fibは、再帰と言って、自分の関数を中で呼び出しており、
フィボナッチ数（1, 1, 2, 3, 5...と前と前々の数字を足して、その数を並べたもの）
を作成しています。
"""

# function multi
def calc_multi(a, b):
        return a * b

# function (再帰)
def calc_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)
    
# 関数呼び出し
print("掛け算:", calc_multi(3, 10))
print("フィボナッチ数:", calc_fib(10))

# %% 例2（関数説明追加）
# function multi
def calc_multi(a, b):
    """
    ２変数の積を計算
    
    Args:
        a int:
            変数1
        b int: 
            変数2
    Returns:
        a*b int:
            入力２変数の積
    """
    return a * b
    
# 関数呼び出し
print("掛け算:", calc_multi(3, 10))