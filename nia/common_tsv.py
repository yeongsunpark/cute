#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-19

header = True
result_list = []
number = 0
f = open("/home/msl/ys/cute/nia/common_tsv/ka.txt", "r")
for line in f:
    if header:
        header = False
        continue
    item = line.split("\t")
    title = item[1]
    context = item[2]
    context_ori = context.replace("|||||","")
    question = item[4]
    answer = item[6]
    # answer_s = context.find("|||||"+answer+"|||||")
    answer_s = context.find("|||||"+answer+"|||||")
    answer_e = answer_s + len(answer)
    extract_answer = context_ori[answer_s:answer_e]
    number +=1
    if answer != extract_answer:
        result_list.append([title, context, str(number), question, answer, "", "", context_ori, str(answer_s), str(answer_e)])
        print (answer_s)
        print(answer_e)
        print (answer)
        print (extract_answer)
        break

f.close()
f2 = open("/home/msl/ys/cute/nia/common_tsv/kakao2.txt", "w")
print (len(result_list))
for r in result_list:
    f2.write("\t".join(r))
    f2.write("\n")