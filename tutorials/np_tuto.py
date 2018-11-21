# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 사인과 코사인 곡선의 x,y 좌표를 계산
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 높이가 2이고 너비가 1인 subplot 구획을 설정하고,
# 첫 번째 구획을 활성화.
plt.subplot(2, 1, 1)

# 첫 번째 그리기
plt.plot(x, y_sin)
plt.title('Sine')

# 두 번째 subplot 구획을 활성화 하고 그리기
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# 그림 보이기.

plt.show()