import os, sys
import logging
import ys_logger
import json

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")

json_data = open("work_sql.json", "r")
j = json_data.read()
j = json.loads(j)

f2 = open(j['RM_DUP_ROW']['f4'], "w")  # 안 중복된 데이터  # "rm_dupli_rows4.txt"
f3 = open(j['RM_DUP_ROW']['f5'], "w")  # 중복된 데이터  # "dupli_rows4.txt"
not_dup =  j['CHE_DUP_CON2']['f2']  # check_dupl_conc2 의 결과로 나온 데이터 # "not_dup_head_conc4.txt"

lst = []
with open(not_dup, "r") as f1:
    for line1 in f1:
        item = line1.replace("\n","").split("\t")
        q_1 = item[5]
        answer = item[6]
        context_rm = item[9]
        q_2 = item[13]

        flag = True

        for i in range(len(lst)):
            if q_1 in lst[i][5] and answer in lst[i][6] and context_rm in lst[i][9] and q_2 in lst[i][13]:
                flag = False
                f3.write(line1)
                break
        if flag:
            lst.append(line1.replace("\n","").split("\t"))


for l in lst:
    f2.write("\t".join(l))
    f2.write("\n")
f2.close()
logger.info("All Finish ")