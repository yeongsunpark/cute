import os, sys
import logging
import ys_logger

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")

input_dir = "/home/msl/ys/cute/sams/fortsv"


for f in os.listdir(input_dir):
    cate_list = ["science", "society", "sports", "general", "economy", "ent"]
    for cl in cate_list:
        f2 = str(f)
        if f2.split(".")[0] in [cl] and "final" not in f2:
            print (cl)
            with open(os.path.join(input_dir, f), "r") as f:
                count = 1
                for line in f:
                    item = line.split("\t")

                    with open(os.path.join(input_dir, "final_{}.txt".format(cl)),
                              'a', encoding='utf8') as fp:
                        # fp.write("test")
                        fp.write("\t".join([item[0], item[1], item[2], str(count), item[4], item[6], item[7]]))
                        count +=1