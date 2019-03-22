#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-21

import os

base_dir = "/home/msl/ys/cute/nia/common_tsv/"

result_list = []
number = 1
with open(os.path.join(base_dir, "크웍18전달건_편집_질문번호_ascending.txt"), "r") as f:
    for line in f:
        item = line.split("\t")
        # [title, context, item[2], question, answer, item[5], item[6], plain_context, start, end]
        result_list.append([item[0], item[1], str(number), item[3], item[4], item[5], item[6], item[7], item[8], item[9]])
        number+=1

with open(os.path.join(base_dir, "크웍18전달건_편집_질문번호_ascending_num바꿈.txt"), "w") as f2:
    for rl in result_list:
        f2.write("\t".join(rl))