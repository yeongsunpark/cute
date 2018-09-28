#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class extract():
    def __init__(self):
        self.f = open('sum_txt_2차전달 - 시트5의 사본 (1).tsv', 'r')
        self.f2 = open('sum_txt_2차전달_result.txt', 'w')
        self.data = []

    def f_write(self):
        for line in self.f:
            item = line.split("\t")
            # print (len(item))
            if len(item) == 8:
                content = item[2]
                answer = item[6]
                # answer = answer.replace('"','')
                answer = answer.strip('"')
                # answer = answer
                if "|||||{}|||||".format(answer) in content:
                    content = content.replace("|||||{}|||||".format(answer), "$$$$${}$$$$$".format(answer))
                    # self.f2.write(content)
                    self.f2.write("\t".join([content, answer]))
                else:
                    print ("no : {}".format(answer))
            elif len(item) == 5:
                answer = item[3]
                content = content.replace("|||||{}|||||".format(answer), "$$$$${}$$$$$".format(answer))
            else:
                print ("len error")
            # print (item[0])
            self.f2.write("\n")
        #self.f.close()
        #self.f2.close()


if __name__ == "__main__":
    j = extract()
    j.f_write()