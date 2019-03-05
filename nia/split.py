#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-05

data = "안녕하세요?"
length = 2
data_split = ["".join(x) for x in zip(*[list(data[z::length]) for z in range(length)])]

print (data_split)