import os, sys
import logging
import ys_logger

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


f1 = open("delivered_data/sum.tsv", "r")
# 박영선  a
# 이원문  b
# 카카오  c
# 박영선  d
# 이원문  e
lst = list()
l1 = list
for ff in f1:
    ff = ff.replace("\n", "")
    i = ff.split("\t")
    if len(i) == 9:
        q1 = i[4].strip().replace("?","")
        q2 = i[5].strip().replace("?","")
        ans = i[6].strip()
        l1 = q1, q2, ans
    elif len(i) == 5:
        q1 = i[1].strip().replace("?","")
        q2 = i[2].strip().replace("?","")
        ans = i[3].strip()
        l1 = q1, q2, ans
    lst.append(l1)
f1.close()
logger.info("Finish load f1")


f2 = open("not_dup_head.txt", "w")
f3 = open("dup_head.txt", "w")


with open("select3.txt", "r") as f:
    # 박영선  parkys  a
    # 이원문  moon    b
    # 카카오  kakao   c
    # 박영선  ylunar  x
    # 이원문  moon    y

    for line in f:
        item = line.split("\t")
        q1 = item[5].strip().replace("?","")
        q2 = item[13].strip().replace("?", "")
        ans = item[6].strip()
        flag = True

        for l in lst:
            # for s1, i in zip(select_data1, range(len(select_data1))):
            if q1 == l[0] and q2 == l[1] and ans == l[2]:
                flag = False
                f3.write(line)
                break
        if flag:
            f2.write(line)

f2.close()
f3.close()