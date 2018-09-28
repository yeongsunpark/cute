# -*- coding: utf-8 -*-

import logging
import os, sys

import pymysql

sys.path.append(os.path.abspath('..'))
# import custom_logger
import csv

"""
logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(custom_logger.MyHandler())
logger.info("Finish setting logger")
"""

class SquadDb():

    def __init__(self):
        #self.data_root_dir = "/home/msl/data/mrc/ko_mrc_v8"  # for correction_data
        #self.data_output_dir = "/home/msl/workspace/mrc_minds/output"
        #self.input_data2db = "ko_mrc_v8.0_squad.json"     # for squad2db

        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "msl", "pwd": "msl1234~",
                            "db": "YS_UPDATE_EXERCISE", "encoding": "utf8"}
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
        except Exception as e:
            pass
            # logger.critical(e)
        # logger.info("Finish connecting to database...")

    def update_data(self):
        f = open("q3_1-2000-2.tsv", 'r')

        data = csv.reader(f, delimiter='\t')
        data = list(data)
        for i in range(len(data)):
            try:
                update_memo_sql = 'UPDATE ys_all_qna SET cate1=%s, cate2=%s, cate3=%s WHERE q_id=%s and c_id=%s'
                c_id = data[i][1]
                q_id = data[i][2]
                cate1 = data[i][5]
                cate2 = data[i][6]
                cate3 = data[i][7]
                self.cur.execute(update_memo_sql, (cate1, cate2, cate3, q_id, c_id))
                self.con.commit()
                # print "update success"
            except:
                print "try"

    def insert_data(self):
        print 'insert start'
        f = open("q_id_6(category_error).tsv", 'r')
        data = csv.reader(f, delimiter='\t')
        data = list(data)
        for i in range(len(data)):
            try:
                insert_memo_sql = 'insert into memo (conum, user_id, comment, uploadtime) values(%s,%s,%s,%s)'
                after = data[i][0]
                before = data[i][1]
                self.cur.execute(insert_memo_sql, (205, after, before, datetime.now()))
                self.con.commit()
            except:
                print "try again"

    def count_data(self):
        print 'count start'
        try:
            count_memo_sql = 'select count(*) from ys_all_qna'
            self.cur.execute(count_memo_sql)
            select_count_row = self.cur.fetchall()
            print select_count_row
            self.con.commit()
        except:
            print "cannnot user_information"

if __name__ == "__main__":
    j = SquadDb()
    j.connect_db()
    j.update_data()
    # j.count_data()
    # j.insert_data()
    # logger.info("All finished")
