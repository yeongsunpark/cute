import os, sys
import logging
import ys_logger

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

with open("not_dup_head_conc4.txt", "r") as f1:
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
