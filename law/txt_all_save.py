#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re

sys.path.insert(0,'..')

input_dir = "/home/msl/ys/cute/law/data4_out"
data = []
# 하기 전에 txt 파일이 utf-8로 인코딩이 되어 있나 꼭 확인하기!
# utf-8 파일은 제일 윗 줄을 제대로 인식을 못하니 한 줄 띄기!

f2 = open("/home/msl/ys/cute/law/finish4.txt", "w")
for f in os.listdir(input_dir):
    with open(os.path.join(input_dir, f), "r") as f:
        for line in f:
            f2.write(line)
        f2.write("\n")
f2.close()