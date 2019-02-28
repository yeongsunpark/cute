#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-27

import sys, os
import json
import time

sys.path.insert(0,'..')

input_file = "/home/msl/ys/cute/nia/cw18.txt"
only_file = "/home/msl/ys/cute/nia/cw18_only.txt"
dup_file = "/home/msl/ys/cute/nia/cw18_dup.txt"

f2 = open(only_file, "w")
f3 = open(dup_file, "w")
# title content 질문번호    질문  유사질문    답변  기사일자    원본  답시작 답끝
lst = []
print (time.time)
with open(input_file, "r") as f1:
    for line1 in f1:
        item = line1.replace("\n", "").split("\t")

        # print (len(item))
        if len(item) == 10:
            q_1 = item[3]
            answer = item[5]
            context = item[7]

            if 2000 > len(context) >=300:

                flag = True

                for i in range(len(lst)):
                    if q_1 in lst[i][3] and answer in lst[5] and context in lst[7]:
                        flag =False
                        f3.write(line1)
                        break
                if flag:
                    lst.append(line1.replace("\n","").split("\t"))
            else:
                pass

for l in lst:
    f2.write("\t".join(l))
    f2.write("\n")
f2.close()
print (time.time)