import os, sys
import logging
import ys_logger

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")

f2 = open("rm_dupli_rows.txt", "w")

lst = []
with open("new_emails.txt", "r") as f1:
    for line1 in f1:
        item = line1.replace("\n","").split("\t")
        name = item[0]
        alpha = item[2]

        flag = True

        for i in range(len(lst)):
            if name in lst[i][0] and alpha in lst[i][2]:
                flag = False
                break
        if flag:
            lst.append(line1.replace("\n","").split("\t"))
            # for i in range(len(lst)):
                # print (lst[i][0])
print (lst)
for l in lst:
    f2.write("\t".join(l))
    f2.write("\n")
f2.close()  