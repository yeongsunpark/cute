# -*- coding: utf-8 -*-
import numpy as np
import torch
"""
# N은 배치 크기이며, D_in은 입력의 차원입니다;
# H는 은닉 계층의 차원이며, D_out은 출력 차원입니다:
N, D_in, H, D_out = 8, 20, 10, 1

# 무작위의 입력과 출력 데이터를 생성합니다.
x = np.random.randn(N, D_in)  # (64(배치 크기), 1000(입력의 차원))

y = np.random.randn(N, D_out)  # (64(배치 크기), 10(출력의 차원))

# 무작위로 가중치를 초기화합니다.
w1 = np.random.randn(D_in, H)  # (1000(입력의 차원), 100(은닉 계층의 차원))
w2 = np.random.randn(H, D_out)  # (100(은닉 계층의 차원), 10(출력 차원))

learning_rate = 1e-6
for t in range(2):
    # 순전파 단계: 예측값 y를 계산합니다.
    h = x.dot(w1)  # 벡터의 내적이나 매트릭스의 벡터 곱이나, 메트릭스 곱을 계산. v[0]*w[0] + v[1]*w[1] = 219
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    # 손실(loss)을 계산하고 출력합니다.
    loss = np.square(y_pred - y).sum()
    print(t, loss)

    # 손실에 따른 w1, w2의 변화도를 계산하고 역전파합니다.
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # 가중치를 갱신합니다.
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
"""


dtype = torch.float
device = torch.device("cpu")
# dtype = torch.device("cuda:0") # GPU에서 실행하려면 이 주석을 제거하세요.

# N은 배치 크기이며, D_in은 입력의 차원입니다;
# H는 은닉 계층의 차원이며, D_out은 출력 차원입니다.
N, D_in, H, D_out = 64, 1000, 100, 10

# 무작위의 입력과 출력 데이터를 생성합니다.
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

# 무작위로 가중치를 초기화합니다.
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(500):
    # 순전파 단계: 예측값 y를 계산합니다.
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    # 손실(loss)을 계산하고 출력합니다.
    loss = (y_pred - y).pow(2).sum().item()
    print(t, loss)

    # 손실에 따른 w1, w2의 변화도를 계산하고 역전파합니다.
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # 경사하강법(Gradient Descent)를 사용하여 가중치를 갱신합니다.
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2