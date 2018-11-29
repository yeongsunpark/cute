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
final_dir = j['SAVE_AS']['final_dir']

try:
    if not(os.path.isdir(final_dir)):
        os.makedirs(os.path.join(final_dir))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


with open(clean, "r") as f1:
    for line1 in f1:
        if header:
            header = False
            continue

        item = line1.split("\t")
        q_id = item[4]
        category = q_id.split("_")[2]

        if category == "science":
            science.append(line1)
        elif category == "society":
            society.append(line1)
        elif category == "sports":
            sports.append(line1)
        elif category == "general":
            general.append(line1)
        elif category == "economy":
            economy.append(line1)
        elif category == "ent":
            ent.append(line1)
        else:
            logger.error("NO CATEGORY")
            break

"""
with open("science.txt", "w") as f2:
    for l in science:
        item = l.split("\t")
        # f2.write(l)
        f2.write("\t".join([item[0], item[1]]))
        f2.write("\n")
"""

category_list = [science, society, sports, general, economy, ent]
str_category_list = ["science", "society", "sports", "general", "economy", "ent"]

for cl1, cl2 in zip(category_list, str_category_list):
    with open(os.path.join(final_dir, "{}.txt".format(cl2)), 'w', encoding='utf8') as f2:
    # with open("{}.txt".format(cl2), "w") as f2:
        for l in cl1:
            item = l.split("\t")
            # c_id, title, context(marker), q_id_1, question_1, q_id_2, question_2, answer
            f2.write("\t".join([item[0], item[1], item[14], item[4], item[5], item[12], item[13], item[6]]))
            f2.write("\n")