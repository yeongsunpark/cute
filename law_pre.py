#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re
import csv

sys.path.insert(0,'..')

input_dir = "/home/msl/ys/cute/"
output_dir = "/home/msl/ys/cute/output/finish_3.tsv"
f2 = open(output_dir, 'w', encoding='utf-8', newline='')
wr = csv.writer(f2, delimiter='\t')

title_index = 232
context_index = 9152

p = re.compile('<br>')
revision = re.compile(# '<개정 *\d+[.] *\d+[.] *\d+[.][,] *\d+[.] *\d+[.] \d*[.]>|'
                      '<개정( *\d+[.] *\d+[.] *\d+[.][,])+ *\d+[.] *\d+[.] \d*[.]>|'
                      '<(개정|신설) *\d+[.] *\d+[.] *\d+[.]([,] *\d+[.] *\d+[.] *\d+[.])*>|'
                      '[[](전문개정|제목개정|본조신설) *\d+[.] *\d+[.] * \d+[.]]|'
                      '[[]시행일 *[:] *\d+[.] *\d+[.] *\d+[.]*]|'                   
                      '[[]제\d+조(의\d)*에서 이동.*]|'
                      '[[]종전 제\d+조(의\d+)*는 제\d+조(의\d+(으)*)*로 이동.*]|'
                      '제\d*. 삭제 *<\d+[.]* \d+[.]* \d+[.]>|'  # 9/17 add
                      '제\d*조의\d*. 삭제 *<\d+[.]* \d+[.]* \d+[.]>|'  # 9/17 add
                      '[제\d조 및 ]*제\d*조 생략|'  # 9/17 modi
                      '제\d*조부터 제\d조*까지 생략|'  # 9/17 add
                      '(제\d조[(]시행일[) ])*이 법은 (.)*부터 시행한다[.].*|'  # 9/17 add
                      '. 삭제 *<\d+[.]* \d+[.]* \d+[.]>|'
                      '[[]\d+[.] *\d+[.] *\d+[.] *법률 제\d+.*삭제함.]|'
                      '[[]법률 제\d+호[(]\d+[.] *\d+[.] *\d+[.][)].*규정에 의하여 .*\d일까지 유효함]|'
                      '<단서 생략>')

pre_title = "희귀질환관리법"
with open(os.path.join(input_dir, "finish3.txt"), "r") as f:
    for line in f:
        line = p.sub('', line)
        line = line.replace('  ', ' ')
        item = line.split("\t")

        title = item[0].replace("\n", "")
        if title == pre_title:
            title_index = title_index
        else:
            pre_title = title
            title_index = title_index+1
        jang = item[1].replace("\n", "")
        jeol = item[3].replace("\n", "")
        jo = item[5].replace("\n", "")

        if revision.search(jo):
            jo = revision.sub('', jo)

        context_index += 1
        if len(jo.replace(" ","")) > 40:
            wr.writerow([title_index, title, jang, jeol, context_index, jo, len(jo.replace(" ",""))])
f2.close()