#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by yeongsunpark at 2019-02-27

import sys, os
import json

sys.path.insert(0,'..')

input_dir = "/home/msl/ys/cute/nia/cw18"
output_file = "/home/msl/ys/cute/nia/cw18.txt"

f2 = open(output_file, "w")
for f in os.listdir(input_dir):
    with open(os.path.join(input_dir, f), "r") as f:
        for line in f:
            f2.write(line)
        f2.write("\n")
f2.close()

