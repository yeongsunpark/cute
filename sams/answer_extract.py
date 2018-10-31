#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class extract():
    def __init__(self):
        self.f = open('/home/msl/ys/cute/sams/select3.txt', 'r')
        self.f2 = open('/home/msl/ys/cute/sams/select3_right.txt', 'w', newline="")
        self.f3 = open('/home/msl/ys/cute/sams/select3_wrong.txt', 'w')
        self.data = []

    def f_write(self):
        for line in self.f:
            item = line.split("\t")
            # print (len(item))
            if len(item) == 9:
                content = item[2]
                answer = item[5]
                answer = answer.strip('"')
                # if "|||||{}|||||".format(answer) in content:
                if "{}".format(answer) in content:
                    per_content = content.replace("|||||{}|||||".format(answer), "%%%%%{}%%%%%".format(answer))
                    per_start = per_content.find("%%%%%{}%%%%%".format(answer))
                    # self.f2.write(content)
                    # self.f2.write("\t".join([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], per_content]))
                    self.f2.write("\t".join([line.replace("\n",""), per_content, str(per_start)]))
                    self.f2.write("\n")
                else:
                    self.f3.write(line)
            # self.f2.write("\n")
        self.f.close()
        self.f2.close()
        self.f3.close()


if __name__ == "__main__":
    j = extract()
    j.f_write()