# -*- coding: utf-8 -*-

import logging
import os, sys

import pymysql

sys.path.append(os.path.abspath('..'))
# import custom_logger
import csv



class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "root", "pwd": "data~secret!",
                            "db": "SQUAD_KO_ORI", "encoding": "utf8"}
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
    def select_data(self):
        f = open("how-2.txt", "r")
        f2 = open("how-2_result.txt", "w")
        data = csv.reader(f, delimiter='\t')
        data = list(data)
        for i in range(len(data)):
            try:
                # select_sql = 'select c_id, q_id, question, answer from SQUAD_KO_ORI.all_qna WHERE q_id =%s'
                select_sql2 = 'select context from SQUAD_KO_ORI.all_context WHERE q_id =%s'
                q_id = data[i][1]
                print (q_id)
                # self.cur.execute(select_sql, (q_id))
                self.cur.execute(select_sql2, (q_id))
                select_data_row = self.cur.fetchall()
                # print (select_data_row)
                self.con.commit()
                f2.write(select_data_row[0][2])
                f2.write("\n")
            except:
                print ("no")

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
                print ("try")

    def insert_data(self):
        print ('insert start')
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
                print ("try again")

    def count_data(self):
        print ('count start')
        try:
            count_memo_sql = 'select count(*) from all_qna'
            self.cur.execute(count_memo_sql)
            select_count_row = self.cur.fetchall()
            print (select_count_row)
            self.con.commit()
        except:
            print ("cannnot user_information")

if __name__ == "__main__":
    j = SquadDb()
    j.connect_db()
    j.select_data()
    # j.update_data()
    # j.count_data()
    # j.insert_data()
    # logger.info("All finished")
