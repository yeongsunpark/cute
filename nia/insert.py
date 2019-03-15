#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-03-05

import logging
import os, sys

import pymysql

sys.path.append(os.path.abspath('..'))
# import custom_logger
import csv

NUM_USER = 25

class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "root", "pwd": "data~secret!",
                            "db": "MRC_TRAIN", "encoding": "utf8"}
        self.con = None
        self.cur = None
        self.connect_db()

    def easy_mysql(self, cfg_dict, encoding='utf8', autocommit=False):
        self.con = pymysql.connect(host=cfg_dict['host'], user=cfg_dict['usr'],
                                   passwd=cfg_dict['pwd'], db=cfg_dict['db'], charset=encoding)
        self.cur = self.con.cursor()
        if autocommit is True:
            self.con.autocommit(True)

    def connect_db(self):
        try:        # try to connect to project db
            cfg_dict = dict(host=self.db_cnf_dict['host'], usr=self.db_cnf_dict['usr'],
                            pwd=self.db_cnf_dict['pwd'], db=self.db_cnf_dict['db'])
            self.easy_mysql(cfg_dict, encoding=self.db_cnf_dict['encoding'], autocommit=True)     # turn-on autocummit, be careful!
            self.cur.execute("SET NAMES utf8")
            print ("hi")
        except Exception as e:
            pass


    def insert_data(self, max_category_id):
        print ('insert start')
        f = open("/home/msl/ys/cute/nia/db_news/fin_jul2dec2.txt", 'r')
        data = csv.reader(f, delimiter='\t')
        data = list(data)
        # max_category_id = 613
        max_c_id = max_category_id
        max_c_id = max_c_id+1
        for i in range(len(data)):
            try:
                insert_memo_sql = 'INSERT INTO DATA_CONTEXT_TB (category_id, text, morpheme, status, target_user_id) values(%s,%s,%s,%s, %s)'
                category_id = max_c_id
                text = str(data[i][1]).strip('"')
                # morpheme = data[i][2]  #test
                morpheme = "test"
                # status = data[i][3]  #RD
                status = "RD"
                target_user_id = 'user' + str(i%NUM_USER+1)  #user1-20


                self.cur.execute(insert_memo_sql, (category_id, text, morpheme, status, target_user_id))
                self.con.commit()
                max_c_id += 1
            except:
                print ("try again")

    def count_data(self):
        print ('count start')
        try:
            count_memo_sql = 'select count(*) from DATA_CONTEXT_TB'
            self.cur.execute(count_memo_sql)
            select_count_row = self.cur.fetchall()
            print (select_count_row)
            self.con.commit()
        except:
            print ("cannnot user_information")


    def max_category_id(self):
        print ('max_category_id start')
        try:
            count_memo_sql = 'SELECT max(category_id) FROM MRC_TRAIN.DATA_CONTEXT_TB'
            self.cur.execute(count_memo_sql)
            select_count_row = self.cur.fetchall()
            print (select_count_row[0][0])
            print (type(select_count_row[0][0]))
            self.con.commit()
        except:
            print ("cannnot user_information_MAX")
        return select_count_row[0][0]


if __name__ == "__main__":
    j = SquadDb()
    j.connect_db()
    # j.select_data()
    # j.update_data()
    mx = j.max_category_id()
    ist = j.insert_data(mx)
    # j.insert_data()
    # logger.info("All finished")
