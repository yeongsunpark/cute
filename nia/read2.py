#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-21

import os

base_dir = "/home/msl/ys/cute/nia/common_tsv/"

result_list = []
with open(os.path.join(base_dir, "크웍18전달건_편집_질문번호_error.txt"), "r") as f:
    for line in f:
        item = line.split("\t")
        # [title, context, item[2], question, answer, item[5], item[6], plain_context, start, end]
        title = item[0]
        context = item[1]
        q_id = item[2]
        question = item[3]
        answer = item[4]
        # plain_context = item[7]
        plain_context = context.replace("|||||", "")
        answer_s = context.find("|||||" + answer + "|||||")
        answer_e = answer_s + len(answer)
        extract_answer = plain_context[answer_s:answer_e]

        if answer != extract_answer:
            print(line)
            print (answer)
            print (extract_answer)
            print (answer_s)
            print(answer_e)
            break
        else:
            result_list.append([title, context, q_id, question, answer, "", "", plain_context, str(answer_s), str(answer_e)])

with open(os.path.join(base_dir, "크웍18전달건_편집_질문번호_correct.txt"), "w") as f2:
    for r in result_list:
        f2.write("\t".join(r))
        f2.write("\n")