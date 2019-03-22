#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-06

import os
import logging


# f2 = open("/home/msl/ys/cute/nia/no_marker/error_checker.tsv","w")
# f3 = open("/home/msl/ys/cute/nia/no_marker/normal_checker.tsv","w")


# 알바분이 수정해 주신 거.

# num = 1
for f in os.listdir("/home/msl/ys/cute/nia/modi_che"):
    if "no_checker" not in f:
        continue
    if "yjs" not in f:
        continue
    creator = f.split("_")[2].split(".")[0]
    logging.error(creator)
    f2_list = []
    f3_list = []

    # f = open("no_checker.tsv", "r")
    with open(os.path.join("/home/msl/ys/cute/nia/modi_che", f), "r") as f:
        t = ""
        l = ""

        for line in f:
            item = line.split("\t")
            content = item[5].replace("\n","")  # 컨텐츠에 본문 넣고
            answer = item[4]

            a = content.count("|||||"+answer+"|||||")  # 컨텐츠에서 answer 가 몇 개 있는지 찾을 건데
            if a != 1:  # 일이 아니면 ㅋㅋㅋ 오류야!!!
                print (line)
                break

            elif a == 1:
                start = (content.find("|||||"+answer+"|||||"))
                plain_context = content.replace("|||||","")
                # f3_list.append([t, m_context, str(num), item[2], item[3], item[4], l, str(start), str(a), str(a + len(answer))])
                f3_list.append([item[0], content, str(item[1]), item[3], item[4], "", "", plain_context, str(start), str(start + len(answer))])

                with open(os.path.join("/home/msl/ys/cute/nia/modi_che/", "normal2_{}.tsv".format(creator)),
                          'w', encoding='utf8') as f3:
                    for fl in f3_list:
                        # for ff in fl:
                        f3.write("\t".join(fl))
                        f3.write("\n")
            else:
                print(line)
                print (a)
                break
            # num += 1


    f.close()
# f2.close()
# f3.close()