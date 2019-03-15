#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-28

import math
import random
import json


with open("didi.json", 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)
    data = json_data1['data']

# random_key = random.sample(json_data1['data'], 50)[0]


a_cnt = math.floor((len(data)) * 0.7)
a = random.sample(data, a_cnt)
# print (len(a))

b_tmp = [c for c in data if c not in a]
b_cnt = math.floor((len(data)-len(a)) * 0.5)
b = random.sample(b_tmp, b_cnt)
# print (len(b))

c_tmp = [c for c in data if c not in a and c not in b]
# print (len(c_tmp))

# print (type(json_data1))

with open("d80.json", 'w', encoding='utf-8') as wf:
    json.dump(a, wf, ensure_ascii=False, indent=2)

"""
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