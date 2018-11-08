import os, sys
import logging
import concurrent.futures
import ys_logger

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


f1 = open("delivered_data/sum.tsv", "r")
f2 = open("not_dup_head_conc.txt", "w")
f3 = open("dup_head_conc.txt", "w")
lst = list()


def preproc():
    l1 = list
    for ff in f1:
        ff = ff.replace("\n", "")
        i = ff.split("\t")
        if len(i) == 9:
            q1 = i[4].strip().replace("?", "")
            q2 = i[5].strip().replace("?", "")
            ans = i[6].strip()
            l1 = q1, q2, ans
        elif len(i) == 5:
            q1 = i[1].strip().replace("?", "")
            q2 = i[2].strip().replace("?", "")
            ans = i[3].strip()
            l1 = q1, q2, ans
        lst.append(l1)
    f1.close()
    logger.info("Finish load f1")

def comp(lenf, n ,r):
    logger.info("processing: {} ..< {}".format(n, n + r))
    for line in lenf[n:n + r]:
        item = line.split("\t")
        q1 = item[5].strip().replace("?", "")
        q2 = item[13].strip().replace("?", "")
        ans = item[6].strip()
        flag = True

        for l in lst:
            if q1 == l[0] and q2 == l[1] and ans == l[2]:
                flag = False
                f3.write(line)
                break
        if flag:
            f2.write(line)

def main2():
    workers = 10
    r = 1000
    with open("select3.txt", "r") as f:
        lenf = f.readlines()
        lenf = tuple(lenf)
        print(len(lenf))
        # self.comp(lenf, 0, r)
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as exe:
            fs = {exe.submit(comp, lenf, n, r) for n in range(0, len(lenf), r)}

    logger.info("Finish All")
    f2.close()
    f3.close()


if __name__ == "__main__":
    preproc()
    main2()