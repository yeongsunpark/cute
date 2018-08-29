#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re

sys.path.insert(0,'..')

input_dir = "/home/msl/ys/cute/data"
output_dir = "/home/msl/ys/cute/data"
inout = "c22_raw"
input_file = os.path.join(input_dir,"{}.txt").format(inout)
output_file = os.path.join(output_dir,"{}_output.txt").format(inout)

title = re.compile('[[].*')
test = re.compile('.*조')
revision = re.compile(# '<개정 *\d+[.] *\d+[.] *\d+[.][,] *\d+[.] *\d+[.] \d*[.]>|'
                      '<개정( *\d+[.] *\d+[.] *\d+[.][,])+ *\d+[.] *\d+[.] \d*[.]>|'
                      '<(개정|신설) *\d+[.] *\d+[.] *\d+[.]([,] *\d+[.] *\d+[.] *\d+[.])*>|'
                      # '<(개정|신설) *\d+[.] *\d+[.] *\d+[.]>|'
                      '[[](전문개정|제목개정|본조신설) *\d+[.] *\d+[.] * \d+[.]]|'
                      # '[[]전문개정 *\d+[.] *\d+[.] * \d+[.]]|'
                      # '[[]제목개정 *\d+[.] *\d+[.] * \d+[.]]|'
                      # '[[]본조신설 *\d+[.] *\d+[.] * \d+[.]]|'
                      '[[]시행일 *[:] *\d+[.] *\d+[.] *\d+[.]*]|'
                      # '[[]시행일 *[:] *\d+[.] *\d+[.] *\d+]|'                      
                      '[[]제\d+조(의\d)*에서 이동.*]|'
                      '[[]종전 제\d+조(의\d+)*는 제\d+조(의\d+(으)*)*로 이동.*]|'
                      # '[[]종전 제\d+조는 제\d+조로 이동.*]|'
                      # '[[]종전 제\d+조의\d+는 제\d+조의\d+(으)*로 이동.*]|'
                      '. 삭제 *<\d+[.]* \d+[.]* \d+[.]>'
                      '[[]\d+[.] *\d+[.] *\d+[.] *법률 제\d+.*삭제함.]'
                      '[[]법률 제\d+호[(]\d+[.] *\d+[.] *\d+[.][)].*규정에 의하여 .*\d일까지 유효함]'
                      '<단서 생략>')

test = re.compile('[[]시행일 *[:] *\d+[.] *\d+[.] * \d+[.]]')
after = ('다. $를 다.로 바꾸기 / 제 *\d *조 *$ 를 없애기')

with open (input_file, "r") as f:
    data = []
    for line in f:
        # print (line)
        if revision.search(line):
            print (line)
            new = revision.sub('', line)
            data += new
        else:
            data += line

with open (output_file, "w") as f2:
    f2.write("".join(data))