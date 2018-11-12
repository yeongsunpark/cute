import os, sys
import logging
import ys_logger
import json

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


f1 = open("/home/msl/ys/cute/sams/delivered_cw/ko_mrc_cw_v1_squad_pretty.json", "r")  # 전달 한 거
json_data1 = json.load(f1)
# 박영선  a
# 이원문  b
# 카카오  c
# 박영선  d
# 이원문  e
lst = list()
l1 = list
for doc in json_data1['data']:
    for t, p in zip(doc["title"], doc["paragraphs"]):
        context = p["context_ori"]
        for qa in p["qas"]:
            q_id = qa['id']
            if '-1' in str(qa['id']):
                question1 = qa['question'].strip("'").strip('"')
                text = qa['answers'][0]['text']
            # elif "-2" in str(qa['id']):
                # question2 = qa['question'].replace("?","")
                l1 = question1, text
    lst.append(l1)
f1.close()
logger.info("Finish load f1")


f2 = open("not_dup_cw.txt", "w")
f3 = open("dup_cw.txt", "w")
f4 = open("dup_len.txt","w")


with open("/home/msl/data/mrc/ko_cw/sum.txt", "r") as f:  # 전달 안 한 거
    # 박영선  parkys  a
    # 이원문  moon    b
    # 카카오  kakao   c
    # 박영선  ylunar  x
    # 이원문  moon    y

    for line in f:
        item = line.split("\t")
        if len(item) == 10:
            q1 = item[3].strip("'").strip('"')
            ans = item[5].strip("'")
            flag = True

            for l in lst:
                # for s1, i in zip(select_data1, range(len(select_data1))):
                if q1 == l[0] and ans == l[1]:
                    flag = False
                    f3.write(line)
                    break
            if flag:
                f2.write(line)
        else:
            f4.write (line)

f2.close()
f3.close()
f4.close()
logger.info("Finish All")
