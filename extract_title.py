#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class extract():
    def __init__(self):
        self.f = open('card.txt', 'r')
        self.f2 = open('card_result.txt', 'w')
        self.data = []

    def f_write(self):
        for line in self.f:
            item = line.split(";;;;;")
            # print (item[0])
            self.f2.write(item[0])
            self.f2.write("\n")
        #self.f.close()
        #self.f2.close()


if __name__ == "__main__":
    j = extract()
    j.f_write()