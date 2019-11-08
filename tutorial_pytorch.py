# ref to https://kokensha.xyz/deeplearning/pytorch-mnist-handwritten-digits-tutorial/

# %% library install
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST

# %% dataset download
mnist_data = MNIST('~/tmp/mnist', train=True, download=True, transform=transforms.ToTensor())
data_loader = DataLoader(mnist_data,batch_size=4,shuffle=False)

# %% read example data
data_iterator = iter(data_loader)
images, labels = data_iterator.next()

# %% visualize example data
data = images[2].numpy()
plt.imshow(data.reshape(28, 28), cmap='inferno', interpolation='bicubic')
plt.show()
print('ラベル:', labels[0])



# %% read training data and test ata
# training data
train_data_with_label = MNIST('~/tmp/mnist', train=True, download=True, transform=transforms.ToTensor())
train_data_loader = DataLoader(train_data_with_label,batch_size=4,shuffle=True)
# test data
test_data_with_label = MNIST('~/tmp/mnist', train=False, download=True, transform=transforms.ToTensor())
test_data_loader = DataLoader(test_data_with_label,batch_size=4,shuffle=False)

# %% define deep learning model
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
 
class MLP(nn.Module):
  def __init__(self):
    super().__init__()
    #入力層から中間層（隠れ層）
    self.l1 = nn.Linear(28 * 28, 50)
    # 中間層（隠れ層）から出力層
    self.l2 = nn.Linear(50, 10)
        
  def forward(self, x):
    x = x.view(-1, 28 * 28)
    x = self.l1(x)
    x = self.l2(x)
    return x

model = MLP()


# %% define cost function and optimization function
import torch.optim as optimizer
 
# ソフトマックスロスエントロピー
criterion = nn.CrossEntropyLoss()
# SGD
optimizer = optimizer.SGD(model.parameters(), lr=0.01)

# %% training
MAX_EPOCH=4
 
for epoch in range(MAX_EPOCH):
  running_loss = 0.0
  for i, data in enumerate(train_data_loader):
    
    # dataから学習対象データと教師ラベルデータを取り出します
    train_data, teacher_labels = data
    
    # 入力をtorch.autograd.Variableに変換
    train_data, teacher_labels = Variable(train_data), Variable(teacher_labels)
    
    # 計算された勾配情報を削除します
    optimizer.zero_grad()
    
    # モデルでの予測を計算します
    outputs = model(train_data)
    
    # lossとwによる微分計算します
    loss = criterion(outputs, teacher_labels)
    loss.backward()
    
    # 勾配を更新します
    optimizer.step()
    
    # 損失を累計します
    running_loss += loss.data.item()
    
    # 2000ミニバッチずつ、進捗を表示します 
    if i % 2000 == 1999:
      print('学習進捗：[%d, %d]　学習損失（loss）: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
      running_loss = 0.0
        
print('学習終了')


# %% test
import torch
 
count_when_correct = 0
total = 0
#
for data in test_data_loader:
  # dataから評価対象データと教師ラベルデータを取り出します
  test_data, teacher_labels = data
  # 学習したも出rうに評価データを入力し、推定を行う
  results = model(Variable(test_data))
  # 0~9の数字の10クラスに対して、確率が出力されるので、最大の確率のクラスを計算
  _, predicted = torch.max(results.data, 1)
  # 正解値と推定値を比較して、正解した場合はカウントアップする
  total += teacher_labels.size(0)
  count_when_correct += (predicted == teacher_labels).sum()
    
print('正解率：%d / %d = %f'% (count_when_correct, total, int(count_when_correct)/int(total)))


# %% visualize test data
test_iterator = iter(test_data_loader)
# ここで回数を増減して、違うテストデータを取り出せます
test_data, labels = test_iterator.next()
test_data, labels = test_iterator.next()
test_data, labels = test_iterator.next()

results = model(Variable(test_data))
_, predicted_label = torch.max(results.data, 1)
 
plt.imshow(test_data [0].numpy().reshape(28, 28), cmap='inferno', interpolation='bicubic')
print('ラベル：', predicted_label[0])

