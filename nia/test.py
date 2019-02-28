#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-27

import sys, os
import json
import time

sys.path.insert(0,'..')

input_file = "/home/msl/ys/cute/nia/cw18.txt"

dic = {}


with open(input_file, "r") as f1:
    for line1 in f1:
        item = line1.replace("\n", "").split("\t")
        a= len(item)
        if a in dic:
            dic[a] +=1
        else:
            dic[a] = 1

print (dic)