#!/usr/bin/env python
# -*- coding:utf-8 -*-

import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


# 1. CIFAR10를 불러오고 정규화하기
# [0,1] 범위를 갖는 PILImage 이미지를[-1,1] 의 범위로 정규화된 Tensor 로 변환
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)  # train set

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)  # test set

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


# 이미지를 보여주기 위한 함수
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))


# 학습용 이미지를 무작위로 가져오기
dataiter = iter(trainloader)  # image, label 이렇게 두 개로 구성 되어 있음.
images, labels = dataiter.next()

# 이미지 보여주기
imshow(torchvision.utils.make_grid(images))

# 정답(label) 출력
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))


# 2. 합성곱 신경망(Convolution Neural Network) 정의하기
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)  # 3 채널 이미지를 처리할 수 있도록 수정함.
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()

# 3. 손실 함수와 Optimizer 정의하기
criterion = nn.CrossEntropyLoss()  # 분류에 대한 교차 엔트로피 손실(Cross-Entropy loss) 과
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)  # momentum을 갖는 SGD를 사용

# 4. 신경망 학습하기
for epoch in range(2):  # 데이터셋을 두 번 반복하여 신경망을 학습 시킴.
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):  # i 는 index data 는 image 와 label
        # 입력을 받은 후
        inputs, labels = data

        # 변화도(gradient) 매개변수를 0으로 만든 후
        optimizer.zero_grad()

        # 순전파 + 역전파 + 최적화
        outputs = net(inputs)  # x 를 리턴 받음
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # 통계 출력
        running_loss += loss.item()
        if i % 2000 == 1999:  # print every 2000 mini-batches
            print ('[%d, %5d] loss: %.3f' %
                   (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print ('Finished Training')


# 5. 시험용 데이터(test data) 로 신경망 검사하기
dataiter = iter(testloader)
images, labels = dataiter.next()

# print images
imshow(torchvision.utils.make_grid(images))
print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(4)))  # 진짜 정답

outputs = net(images)  # 신경망에 예측 시킴
_, predicted = torch.max(outputs, 1)  # 출력은 10개 분류 각각에 대한 값으로 나타남. 가장 높은 값을 갖은 index 뽑음.

print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                              for j in range(4)))  # 신경망이 예측한 정답

# 전체 데이터셋에 대해서는 어떻게 동작하는지 보기
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))

# 어떤 것들을 더 잘 분류하고, 어떤 것들을 더 못했는지 알아보기
class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i in range(4):
            label = labels[i]
            class_correct[label] += c[i].item()
            class_total[label] += 1

for i in range(10):
    print ('Accuracy of %5s : %2d %%' %(
        classes[i], 100 * class_correct[i] / class_total[i]))



# GPU 에서 학습하기 (신경망을 GPU 로 옮기기)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # CUDA 를 사용할 수 있는 경우 첫 번 째 CUDA 장치를 사용하도로 ㄱ설정
print (device)

net.to(device)  # 재귀적으로 모든 모듈로 가서 매개변수와 버퍼를 CUDA tensor 로 변경
inputs, labels = inputs.to(device), labels.to(device)  # 모든 단계에서 입력과 정답도 GPU 로 보냄


