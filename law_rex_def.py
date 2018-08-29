#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re

sys.path.insert(0,'..')

class law_rex():
    def __init__(self):
        self.input_dir = "/home/msl/ys/cute/data"
        self.output_dir = "/home/msl/ys/cute/data"
        self.inout = "c56_law_data"
        self.input_file = os.path.join(self.input_dir, "{}.tsv").format(self.inout)
        self.output_file = os.path.join(self.output_dir, "{}_output.txt").format(self.inout)

        self.revision = re.compile('<개정 *\d+[.] *\d+[.] *\d+[.][,] *\d+[.] *\d+[.] \d*[.]>|'
                                   '<개정( *\d+[.] *\d+[.] *\d+[.][,])+ *\d+[.] *\d+[.] \d*[.]>|'
                                   '<개정 *\d+[.] *\d+[.] *\d+[.]>|'
                                   '<신설 *\d+[.] *\d+[.] *\d+[.]>|'
                                   '[[]전문개정 *\d+[.] *\d+[.] * \d+[.]]|'
                                   '[[]제목개정 *\d+[.] *\d+[.] * \d+[.]]|'
                                   '[[]본조신설 *\d+[.] *\d+[.] * \d+[.]]|'
                                   '[[]시행일 *[:] *\d+[.] *\d+[.] *\d+[.]]|'
                                   '. 삭제 *<\d+[.]* \d+[.]* \d+[.]>')

        self.test = re.compile('[[]시행일 *[:] *\d+[.] *\d+[.] * \d+[.]]')

    def main(self, mode):
        with open (self.input_file, "r") as f:
            data = []
            for line in f:
                # print (line)
                if self.mode.search(line):
                    # print(line)
                    new = self.mode.sub('', line)
                    data += new
                else:
                    data += line
        with open(self.output_file, "w") as f2:
            print (len(data))
            f2.write("".join(data))

if __name__ == '__main__':
    a = law_rex()
    a.main("law")