import os, sys
import pymysql
import csv
import datetime

sys.path.append(os.path.abspath('..'))


class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "root", "pwd": "data~secret!",
                            "db": "SQUAD_KO_WIKI", "encoding": "utf8"}
        self.con = None
        self.cur = None
        self.connect_db()
        self.f2 = open("select2.txt", "w")
        self.dt = datetime.datetime.now()

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

    def select_data(self):
        print (datetime.datetime.now(), 'select start')
        try:
            # select_sql = 'SELECT c_id, q_id, question, answer, answer_start, (answer_start + CHAR_LENGTH(answer)), CHAR_LENGTH(answer) FROM SQUAD_KO_WIKI.all_qna'
            select_sql = 'SELECT  c.id, c.title, replace(c.context, "|||||", "") AS new_context, ' \
                         'q.q_id, q.question, q.answer, q.answer_start, (q.answer_start + CHAR_LENGTH(q.answer)), CHAR_LENGTH(q.answer) ' \
                         'FROM SQUAD_KO_WIKI.all_qna AS q INNER JOIN SQUAD_KO_WIKI.all_context_ori AS c ON q.c_id = c.id'
            self.cur.execute(select_sql)
            print (datetime.datetime.now(), "1")
            select_data = self.cur.fetchall()
            for sd in select_data:
                if len(sd) == 9:
                    c_id = str(sd[0])
                    title = str(sd[1])
                    new_context = str(sd[2])
                    q_id = str(sd[3])
                    question = str(sd[4])
                    answer = str(sd[5])
                    answer_s = str(sd[6])
                    answer_e = str(sd[7])
                    if "-1" in q_id:
                        self.f2.write("\t".join(c_id, title, new_context, question, answer, answer_s, answer_e))
                    self.f2.write("\n")
                # for s in sd:
                    # self.f2.write(str(s))
                    # self.f2.write("\t")
                # self.f2.write("\n")

            print(datetime.datetime.now(), "2")

        except:
            print ("try again")
            print (self.dt)

    def count_data(self):
        print ('count start')
        try:
            count_sql = 'select count(*) from SQUAD_KO_WIKI.all_qna'
            self.cur.execute(count_sql)
            select_count_row = self.cur.fetchall()
            print (select_count_row)
            self.con.commit()

        except:
            print ("cannnot user_information")

if __name__ == "__main__":
    j = SquadDb()
    j.connect_db()
    j.select_data()
    # j.count_data()
    # logger.info("All finished")