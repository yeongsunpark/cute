#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "Yeongsun Park"
__date__ = "03/05/2018"

import os
import sys
import time
# import logging
sys.path.append(os.path.abspath('..'))
# import custom_logger
from itertools import combinations

class rep_ncr:
    def __init__(self):
        self.required_words = "거래 내역 팩스 외환 계좌 "
        self.option_words = ["ARS", "신청"]
        self.verb = "알려줘"
        self.f1 = "change_word.txt"
        self.f2 = "result.txt"

    def ncr(self):
        string = ""
        for i in range(len(self.option_words)+1):
            output = sum([map(list, combinations(self.option_words, i))], [])
            # output = sum([map(list, combinations(option_words, i)) for i in range(len(option_words) + 1)], [])
            for i in range(0, len(output)):
                string += '\n'
                string += self.required_words
                for j in output[i]:
                    string += j
                    string += ' '
                string += self.verb
        return string

    def rep(self):
        # open("change_word.txt", "r", encoding="utf-8")
        # with open(self.f1, "r", encoding="utf-8") as f1:
        with open(self.f1, "r") as f1:
            fr = f1.readlines()
            change_words = ""
            for line in fr:
                line = line.split(": ")
                if self.verb in line[0]:
                    change_words = line[1]
            change = []
            for change_word in change_words.replace('\n', '').split(', '):
                change.append(change_word)
            # print change
            # logger.info("Find change word")

            # f = open("result.txt", "w", encoding="utf-8")
            with open(self.f2, "w") as f2:
                line = rep_ncr.ncr(self).split('\n')
                for l in line:
                    if self.verb in l:
                        for j in range(len(change)):
                            f2.write(l.replace(self.verb, change[j]))
                            f2.write("\n")
                # logger.info("All Finish")

if __name__ == "__main__":
    j = rep_ncr()
    j.ncr()
    j.rep()