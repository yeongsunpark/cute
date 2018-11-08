import os, sys
import logging
import concurrent.futures
import ys_logger

sys.path.append(os.path.abspath('..'))
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


class CheckDuplConc():

    def __init__(self):
        self.f1 = open("delivered_data/sum.tsv", "r")
        # 박영선  a
        # 이원문  b
        # 카카오  c
        # 박영선  d
        # 이원문  e
        self.f2 = open("not_dup_head_conc.txt", "w")
        self.f3 = open("dup_head_conc.txt", "w")
        self.lst = list()


    def preproc(self):
        l1 = list
        for ff in self.f1:
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
            self.lst.append(l1)
        self.f1.close()
        logger.info("Finish load f1")

    def comp(self, lenf, n ,r):
        for line in lenf[n:n+r]:
            item = line.split("\t")
            q1 = item[5].strip().replace("?", "")
            q2 = item[13].strip().replace("?", "")
            ans = item[6].strip()
            flag = True

            for l in self.lst:
                if q1 == l[0] and q2 == l[1] and ans == l[2]:
                    flag = False
                    self.f3.write(line)
                    break
            if flag:
                self.f2.write(line)
    """
    def main(self):
        with open("select3.txt", "r") as f:
            # 박영선  parkys  a
            # 이원문  moon    b
            # 카카오  kakao   c
            # 박영선  ylunar  x
            # 이원문  moon    y
            self.comp(f)
        logger.info("Finish All")
        self.f2.close()
        self.f3.close()
    """
    def main2(self):
        workers = 2
        r = 10
        with open("select3.txt", "r") as f:
            lenf = f.readlines()
            lenf = tuple(lenf)
            print (len(lenf))
            # self.comp(lenf, 0, r)
            with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as exe:
                fs = {exe.submit(self.comp, lenf, n, r) for n in range(0, len(lenf), r)}

            # check_index(qas, 0, r)
            # with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as exe:
                # fs = {exe.submit(check_index, qas, n, r) for n in range(0, len(qas), r)}

            # 박영선  parkys  a
            # 이원문  moon    b
            # 카카오  kakao   c
            # 박영선  ylunar  x
            # 이원문  moon    y

        logger.info("Finish All")
        self.f2.close()
        self.f3.close()


if __name__ == "__main__":
    a = CheckDuplConc()
    a.preproc()
    a.main2()