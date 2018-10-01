#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import json

sys.path.insert(0,'..')

# input_dir = "/home/msl/ys/cute/law/data4_out"
json_data = open("/home/msl/ys/cute/law/law_parser.json", "r")
d = json_data.read()
d = json.loads(d)
input_dir = d['doc2text_2']['output_dir']
output_file = d['txt_all_save']['output_file']
json_data.close()
# 하기 전에 txt 파일이 utf-8로 인코딩이 되어 있나 꼭 확인하기!
# utf-8 파일은 제일 윗 줄을 제대로 인식을 못하니 한 줄 띄기!

f2 = open(output_file, "w")
for f in os.listdir(input_dir):
    with open(os.path.join(input_dir, f), "r") as f:
        for line in f:
            f2.write(line)
        f2.write("\n")
f2.close()  # 1단계에서 만든 파일들을 하나의 파일로 합침.