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
l = []
with open("cw18_only.txt", "r") as f:
    # title content 질문번호 질문 유사질문 답변 기사일자 원본 답시작 답끝
    for line in f:
        item = line.strip().split("\t")
        if len(item) == 10:

            para_dict = dict()
            para_dict['main_qa_list'] = list()

            title = item[0]
            context_ori = item[7]
            # number += 1
            q_id = item[2]
            q_1 = item[3]
            answer = item[5]
            answer_s = item[8]
            answer_e = item[9]

            qas_dict = dict()
            qas_dict['end'] = answer_e
            qas_dict['begin'] = answer_s
            qas_dict['answer'] = answer
            qas_dict['question'] = q_1
            qas_dict['type'] = 0  # default = 0
            qas_dict['classType'] = "NULL"  # default = NULL
            qas_dict['isFlexible'] = 0

            para_dict['main_qa_list'].append(qas_dict)
            para_dict['text'] = context_ori
            para_dict['seq'] = 0  # default = 0
            para_dict['source'] = 0  # default = 0
            para_dict['sub_doc_type'] = 0 # default = 0
            para_dict['doc_type'] = 0 # default = 0
            para_dict['fileName'] = 0 # default = 0

            if context_ori not in l:
                result['data'].append(para_dict)
                l.append(context_ori)
            else:
                for p in result['data']:
                    if p['text'] == context_ori:
                        p['main_qa_list'].append(qas_dict)

f = open("didi5.json", "w")
json.dump(result, f, ensure_ascii=False, indent=2)