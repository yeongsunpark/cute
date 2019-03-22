#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-21

import os

base_dir = "/home/msl/ys/cute/nia/common_tsv/"

with open(os.path.join(base_dir, "크웍18전달건_편집_질문번호_error.txt", 'r')) as f:
    for line in f:
        item = line.split("\t")


