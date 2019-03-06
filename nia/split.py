#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-05

data = "안녕하세요. 저는 박영선입니다. 만나서 반갑습니다. 잘 지내 봅시다. 나는. 사과를. 먹는다."
# length = 2
# data_split = ["".join(x) for x in zip(*[list(data[z::length]) for z in range(length)])]

# print (data_split)

dd = data.split(". ")
ll =""
a = []
for d in dd:
    if len(a) <= 2:
        a.append(d)
print (a)