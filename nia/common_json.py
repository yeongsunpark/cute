#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-22

import sys, os
import json

base_dir = "/home/msl/ys/cute/nia/common_tsv/"

result = dict()
result['version'] = 1
result['creator'] = "MINDs Lab."
result['data'] = list()
passage_list = list()
number = 1
l = []
with open (os.path.join(base_dir, "no_marker/normal_finish-imbyeonghyeon.tsv"), "r") as f:
    # [title, context, item[2], question, answer, item[5], item[6], plain_context, start, end]
    # title content 질문번호 질문 유사질문 답변 기사일자 원본 답시작 답끝
    for line in f:
        item = line.strip().split("\t")
        if len(item) == 10:
            title = item[0]
            q_id = item[2]
            q_1 = item[3]
            answer = item[4]
            cate = item[5]
            wh = item[6]
            plain_context = item[7]
            answer_s = item[8]
            answer_e = item[9]

            para_dict = dict()
            para_dict['main_qa_list'] = list()

            qas_dict = dict()
            qas_dict['question_type'] = wh  # ex. 1 (수정할 것)
            qas_dict['question'] = q_1
            qas_dict['answer'] = answer
            qas_dict['begin'] = answer_s
            qas_dict['end'] = answer_e
            qas_dict['classType'] = ""  # ex. work_what
            qas_dict['isFlexible'] = 0

            para_dict['main_qa_list'].append(qas_dict)

            para_dict['source'] = cate # ex. 1 (수정할 것)
            para_dict['seq'] = "" # 문서번호
            para_dict['doc_type'] = "" # 단문, 중문, 장문
            para_dict['sub_doc_type'] = "" # 문서 세부 번호
            para_dict['fileName'] = number # 파일명
            para_dict['text'] = plain_context

            if plain_context not in l:
                result['data'].append(para_dict)
                l.append(plain_context)
                number += 1
            else:
                for p in result['data']:
                    if p['text'] == plain_context:
                        p['main_qa_list'].append(qas_dict)

with open (os.path.join(base_dir, "normal_finish-imbyeonghyeon.json"), "w") as f2:
    json.dump(result, f2, ensure_ascii=False, indent=2)