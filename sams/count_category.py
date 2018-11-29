import os, sys
import logging
import ys_logger
import json

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")

header = True
c = dict()
science = []
society = []
sports = []
general = []
economy = []
ent = []

json_data = open("work_sql.json", "r")
j = json_data.read()
j = json.loads(j)
clean = j['RM_DUP_ROW']['f4']  # rm_dupli_rows.py 한 후 깨끗한 데이터

with open(clean, "r") as f1:
    for line1 in f1:
        if header:
            header = False
            continue

        item = line1.split("\t")
        q_id = item[4]
        category = q_id.split("_")[2]

        if category in c:
            c[category] +=1
        else:
            c[category] = 1

print (c)
