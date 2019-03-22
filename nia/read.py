#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-21

import re

error_list = []
normal_list = []
wrong_list = []
number = 0
with open ("/home/msl/ys/cute/nia/common_tsv/크웍18전달건_편집_질문번호.txt") as f:
    for line in f:
        item = line.split("\t")
        if len(item) == 10:
            title = item[0]
            if title.startswith('"') and title.endswith('"'):
                title = title.strip('"')
                title = title.replace('""', '"')

            context = item[1]
            if context.startswith('"') and context.endswith('"'):
                context = context.strip('"')
                context = context.replace('""', '"')

            question = item[3]
            if question.startswith('"') and question.endswith('"'):
                question = question.strip('"')
                question = question.replace('""', '"')

            answer = item[4]
            if answer.startswith('"') and answer.endswith('"'):
                answer = answer.strip('"')
                answer = answer.replace('""', '"')
                # print (answer)
            plain_context = item[7]
            if plain_context.startswith('"') and plain_context.endswith('"'):
                plain_context = plain_context.strip('"')
                plain_context = plain_context.replace('""', '"')
                # print (plain_context)
            plain_context.strip('"').strip()
            start = item[8]
            end = item[9]
            if start == '' or end == '':
                wrong_list.append(item)
                continue
            if plain_context[int(start):int(end)] != answer:
                error_list.append([title, context, item[2], question, answer, plain_context[int(start):int(end)], item[5], item[6], plain_context, start, end])
            elif plain_context[int(start):int(end)] == answer:
                normal_list.append([title, context, item[2], question, answer, item[5], item[6], plain_context, start, end])

with open ("/home/msl/ys/cute/nia/common_tsv/크웍18전달건_편집_질문번호_normal.txt", "w") as f2:
    for el in normal_list:
        f2.write("\t".join(el))
        # f2.write("\n")

with open ("/home/msl/ys/cute/nia/common_tsv/크웍18전달건_편집_질문번호_error.txt", "w") as f3:
    for el in error_list:
        f3.write("\t".join(el))

with open ("/home/msl/ys/cute/nia/common_tsv/크웍18전달건_편집_질문번호_wrong.txt", "w") as f4:
    for el in wrong_list:
        f4.write("\t".join(el))