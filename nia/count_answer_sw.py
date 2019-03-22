#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-06

import os
import logging


# f2 = open("/home/msl/ys/cute/nia/no_marker/error_checker.tsv","w")
# f3 = open("/home/msl/ys/cute/nia/no_marker/normal_checker.tsv","w")

f2_list = []
for f in os.listdir("/home/msl/ys/cute/nia/no_checker"):
    if "no_checker" not in f:
        continue
    creator = f.split("_")[2].split(".")[0]
    logging.error(creator)
    # f2_list = []

    # f = open("no_checker.tsv", "r")
    with open(os.path.join("/home/msl/ys/cute/nia/no_checker", f), "r") as f:
        header = True
        for line in f:
            item = line.split("\t")
            if header:
                header = False
                continue

            q = item[3]
            w5h1 = item[2]
            if w5h1 == "언제":
                w5h1 = 'when'
            elif w5h1 == "어디서":
                w5h1 = "where"
            elif w5h1 == "누가":
                w5h1 = "who"
            elif w5h1 == "무엇을":
                w5h1 = "what"
            elif w5h1 == "어떻게":
                w5h1 = "how"
            elif w5h1 == "왜":
                w5h1 = "why"
            else:
                w5h1 = w5h1

            f2_list.append([q, w5h1])



with open(os.path.join("/home/msl/ys/cute/nia/no_checker/", "sum_sw.tsv"),
            'w', encoding='utf8') as f2:

    rd = dict()
    for fl in f2_list:

        # if fl[1] != "when" and fl[1] != "where" and fl[1] != "who" and fl[1] != "how" and fl[1] != "what" and fl[1] != "why":
            # if fl[1] in rd:
                # rd[fl[1]] +=1
            # else:
                # rd[fl[1]] = 1
    # f2.write(str(rd))


            f2.write("\t".join(fl))
            f2.write("\n")




# f.close()
# f2.close()
# f3.close()