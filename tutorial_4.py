###### Pythonの基礎 #####
# GOAL: 
# ライブラリの関係性を知る

### 独自ライブラリの読み込み方
# %% test_libraryのtest_a.pyをロード（方法１）
import test_library.test_a

# %% test_libraryのtest_a.pyをロード（方法２）
from test_library import test_a

# %% test_libraryのtest_a.pyを名前を変えてロード（方法3）
from test_library import test_a as t_a

# ライブラリの関数やクラスを読み込み
# %% 方法１
test_instance = t_a.test_class_a()

# %% 方法２
from test_library.test_a import test_class_a
test_instance = test_class_a()
