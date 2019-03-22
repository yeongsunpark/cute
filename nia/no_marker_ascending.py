#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-20
"""
lst = [
    ['One', 1],
    ['Three', 3],
]

lst2 = [
    ['Zero', 0],
    ['Two', 2],
]

lst.extend(lst2)

print (lst)

lst.sort(key=lambda x: x[1])
print(lst)
"""
result_list = list()
f = open("/home/msl/ys/cute/nia/no_marker/normal_yeomjisun.tsv" ,"r")
for line in f:
    line = line.replace("\n","")
    item = line.split("\t")
    result_list.append(item)
# print (result_list)
f.close()
f2 = open("/home/msl/ys/cute/nia/modi_che/normal2_work-yjs.tsv", "r")
for line in f2:
    line = line.replace("\n", "")
    item = line.split("\t")
    result_list.append(item)

result_list.sort(key=lambda x: int(x[2]))

f3 = open("/home/msl/ys/cute/nia/modi_che/normal_finish-yeomjisun.tsv", "w")
for rl in result_list:
    f3.write("\t".join(rl))
    f3.write("\n")
