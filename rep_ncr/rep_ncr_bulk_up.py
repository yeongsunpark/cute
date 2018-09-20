#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "Yeongsun Park"
__date__ = "03/05/2018"

import os
import sys
import time
sys.path.append(os.path.abspath('..'))
from itertools import combinations



class rep_ncr:
    def __init__(self, required_words, option_words, interro):
        self.required_words = required_words
        # self.required_words = "거래 내역 팩스 외환 계좌 "
        self.option_words = option_words
        # self.option_words = ["ARS", "신청"]
        self.interro = interro
        # self.interro = "알려줘"
        self.f1 = "change_word.txt"
        self.f2 = "result.txt"

    def ncr(self):
        string = ""
        for i in range(len(self.option_words)+1):
            output = sum([map(list, combinations(self.option_words, i))], [])
            for i in range(0, len(output)):
                string += '\n'
                string += self.required_words
                for j in output[i]:
                    string += j
                    string += ' '
                string += self.interro
        # print string
        return string


    def rep(self):
        with open(self.f1, "r") as f1:
            fr = f1.readlines()
            change_words = ""
            for line in fr:
                line = line.split(": ")
                if self.interro in line[0]:
                    change_words = line[1]
            change = []
            for change_word in change_words.replace('\n', '').split(', '):
                change.append(change_word)

            with open(self.f2, "a") as f2:
                line = rep_ncr.ncr(self).split('\n')
                for l in line:
                    if self.interro in l:
                        for j in range(len(change)):
                            f2.write(l.replace(self.interro, change[j]))
                            f2.write("\n")
                            # print l.replace(self.interro, change[j])
                f2.write("\n")

if __name__ == "__main__":
    input_file = "./input.txt"
    option_words = []
    with open(input_file) as f:
        for line in f:
            item = line.strip().split("\t")
            # print item
            required = item[0]
            all_option = item[1]  # ARS, 신청
            all_option = all_option.split(", ")  # ARS 와 신청으로 나뉘어서 리스트에 넣어짐.
            # repncr = rep_ncr(required, all_option, "알려줘")  # 먼저 class 를 넣고 class 가 __init__ 하는 변수를 넣어줌.
            interro = item[2]
            repncr = rep_ncr(required, all_option, interro)
            # repncr.ncr()  # ncr 에 이상이 있는 거 같으면 이 걸로 단독 실행해주세요.
            repncr.rep()
