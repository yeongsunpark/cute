#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-27

import sys, os
import json
import time

result = dict()
result['version'] = 1
result['creator'] = "MINDs Lab."
result['data'] = list()
passage_list = list()

number = 1
with open("cw18/20180406_gen4.txt", "r") as f:
    # title content 질문번호    질문  유사질문    답변  기사일자    원본  답시작 답끝
    para_dict = dict()
    # para_dict = list()
    for line in f:
        item = line.strip().split("\t")
        if len(item) == 10:
            # result['data'].append(para_dict)
            # new paragraph
            para_dict = dict()
            para_dict['qas'] = list()

            title = item[0]
            context_ori = item[7]

            q_id = item[2]
            q_1 = item[3]
            answer = item[5]
            answer_s = item[8]
            answer_e = item[9]
            id = number
            number +=1

            qas_dict = dict()
            qas_dict['number'] = id
            qas_dict['q_id'] = q_id
            qas_dict['q_1'] = q_1
            qas_dict['answer'] = answer
            qas_dict['answer_s'] = answer_s
            qas_dict['answer_e'] = answer_e

            para_dict['qas'].append(qas_dict)
            para_dict['title'] = title
            para_dict['context'] = context_ori
        result['data'].append(para_dict)

f = open("didi.json", "w")
json.dump(result, f, ensure_ascii=False, indent=2)