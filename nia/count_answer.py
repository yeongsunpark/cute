#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-06

import os


f2 = open("/home/msl/ys/cute/nia/no_marker/error_checker.tsv","w")
f3 = open("/home/msl/ys/cute/nia/no_marker/normal_checker.tsv","w")

for f in os.listdir("/home/msl/ys/cute/nia/no_marker"):
    if "no_checker" not in f:
        continue
    creator = f.split("_")[2].split(".")[0]

    # f = open("no_checker.tsv", "r")
    with open(os.path.join("/home/msl/ys/cute/nia/no_marker", f), "r") as f:
        t = ""
        l = ""
        num = 1

        header = True
        for line in f:
            item = line.split("\t")
            if header:
                header = False
                continue

            if item[1] != "":  # 만약에 공백이 아니라면
                content = item[1]  # 컨텐츠에 본문 넣고
                answer = item[4]
                l = item[1]  # 후를 위해 l에 컨텐츠를 넣어놓음.
                t = item[0]

            elif item[1] == "":  # 만약에 공백이라면
                content = l  # 컨텐츠에 위에 넣은 l 을 넣고.
                # print (content)
                answer = item[4]
            else:
                print(line)
                break

            a = content.count(answer)  # 컨텐츠에서 answer 가 몇 개 있는지 찾을 건데
            if a != 1:  # 일이 아니면 ㅋㅋㅋ 오류야!!!
                f2.write("\t".join([t, str(num), item[2], item[3], item[4], l, str(a)]))
                f2.write("\n")

            elif a == 1:
                start = (l.find(answer))
                m_context = l[:start] + "|" * 5 + answer + "|" * 5 + l[start + len(answer):]
                # f3.write("\t".join([t, l, item[2], item[3], item[4], str(a), str(start), m_context]))
                # title, 본문원본, 육하원칙, 질문, 답변, 본문 안 답변의 개수, 답변의 시작 위치, 마커가 있는 본문
                f3.write("\t".join(
                    [t, m_context, str(num), item[2], item[3], item[4], l, str(start), str(a), str(a + len(answer))]))
                # TITLE	CONTENT	질문번호	질문	답변	기사일자(대신 정답의 수)	원본	답시작위치	답끝위치
                f3.write("\n")
            else:
                print(line)
                break
            num += 1

    f.close()
f2.close()
f3.close()