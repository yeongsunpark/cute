#!/usr/bin/env python
# -*- coding:utf-8 -*-

import torch

# tensor
a = torch.empty (5, 7, dtype=torch.float)  # 초기화 되지 않은 5 * 7 크기의 tensor 생성
a = torch.randn (5, 7, dtype = torch.double)  # 평균 0, 분산 1 의 정규분포를 따르는 무작위 숫자로 double(실수형) tensor 를 초기화.

# In-place / Out-of-place
# tensor 의 모든 In-place 연산은 _ 접미사를 갖는다.
# add 는 연산 결과를 돌려주는 Out-of-place 연산을 하고,
# add_ 는 In-place 연산을 한다.

a.fill_(3.5)  # a 가 값 3.5 로 채워짐. _ 접미사를 가짐. In-place 연산
b = a.add(4.0) # a 는 여전히 3.5. 3.5 + 4.0 = 7.5 의 값이 반환되어 새로운 tensor b 가 된다.

# 0-인덱스(Zero Indexing)
