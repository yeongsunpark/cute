#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-28

import math
import random
contexts = ["일번", "이번", "삼번", "사번", "오번", "육번", "칠번", "팔번", "구번", "십번"]
a_cnt = math.floor((len(contexts)) * 0.7)
a = random.sample(contexts, a_cnt)
print (a)

b_tmp = [c for c in contexts if c not in a]
b_cnt = math.floor((len(contexts)-len(a)) * 0.5)
b = random.sample(b_tmp, b_cnt)
print (b)

c_tmp = [c for c in contexts if c not in a and c not in b]
print (c_tmp)


"""
contexts_not_fix = [c for c in contexts]
contexts_dev_fix = []

test_ratio = 0.75

train_cnt = math.floor((len(contexts)) * (1 - test_ratio))
context_train = random.sample(contexts_not_fix, train_cnt)  # 일번부터 십번 중에 0.9개 뽑아라
print (context_train)

c_dev_tmp1 = [c for c in contexts_not_fix if c not in context_train]
print (c_dev_tmp1)

dev_cnt = math.floor((len(c_dev_tmp1)) * (1 - 0.5))
a_half = random.sample(c_dev_tmp1, dev_cnt)
print (a_half)

b_half = [c for c in dev_cnt not in a_half]
print (b_half)



c_dev_tmp2 = list(contexts_dev_fix)
print (c_dev_tmp2)

# logger.info("c_dev_tmp1: {}".format(len(c_dev_tmp1)))
# logger.info("c_dev_tmp2: {}".format(len(c_dev_tmp2)))
context_dev = c_dev_tmp1 + c_dev_tmp2
print (context_dev)

# logger.info("train_cnt: {}".format(train_cnt))
# logger.info("Len context_train: {}".format(len(context_train)))
# logger.info("Len context_dev: {}".format(len(context_dev)))
"""