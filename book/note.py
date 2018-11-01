#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1. tuple list 로 dict 생성
person = [('kim', 30), ('hong', 35), ('kang', 25)]
print (type(person))
mydict = dict(person)

# 2. key = value 파리미터로부터 dict 생성
scores = dict(a = 80, b = 90, c = 100)
print (scores['b'])
