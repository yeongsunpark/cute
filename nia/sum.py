#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-13


import sys, os
import json

sys.path.insert(0,'..')


# input_dir = "/home/msl/ys/cute/law/data4_out"
input_dir = "/home/msl/ys/cute/nia/input"
output_file = "/home/msl/ys/cute/nia/cw19.json"
# 하기 전에 txt 파일이 utf-8로 인코딩이 되어 있나 꼭 확인하기!
# utf-8 파일은 제일 윗 줄을 제대로 인식을 못하니 한 줄 띄기!


result = dict()
result['version'] = 1
result['creator'] = "MINDs Lab."
result['data'] = list()

f2 = open(output_file, "w")
for f in os.listdir(input_dir):
    with open(os.path.join(input_dir, f), "r") as f:
        json_data1 = json.load(f)
        result['data'].append(json_data1)


with open ("cw19.json","w") as f2:
    json.dump(result, f2, indent=2, ensure_ascii=False)
