import os, sys
import pymysql
import csv
import datetime
import csv

sys.path.append(os.path.abspath('..'))


class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "root", "pwd": "data~secret!",
                            "db": "SQUAD_KO_WIKI", "encoding": "utf8"}
        self.con = None
        self.cur = None
        self.connect_db()
        self.f2 = open("select3.txt", "w", newline="")
        self.q_id_1 =""
        self.q_id_2 =""
        self.question_1 = ""
        self.question_2 = ""
        self.result_list = []

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
            select_sql = 'SELECT  c.id, c.title, c.context, ' \
                         'q.q_id, q.question, q.answer, q.answer_start, (q.answer_start + CHAR_LENGTH(q.answer)), CHAR_LENGTH(q.answer) ' \
                         'FROM SQUAD_KO_WIKI.all_qna AS q INNER JOIN SQUAD_KO_WIKI.all_context_ori AS c ON q.c_id = c.id'
            self.cur.execute(select_sql)
            print (datetime.datetime.now(), "1")
            select_data = self.cur.fetchall()
            for sd in select_data:
                for s in sd:
                    self.f2.write(str(s))
                    self.f2.write("\t")
                self.f2.write("\n")

            print(datetime.datetime.now(), "2")

        except:
            print ("try again")
            print (self.datetime.datetime.now())

    def select_data2(self):
        print (datetime.datetime.now(), 'select start')
        # select_sql = 'SELECT c_id, q_id, question, answer, answer_start, (answer_start + CHAR_LENGTH(answer)), CHAR_LENGTH(answer) FROM SQUAD_KO_WIKI.all_qna'
        """
        select_sql = 'SELECT  c.id, c.title, c.context, ' \
                     'q.q_id, q.question, q.answer, q.answer_start, (q.answer_start + CHAR_LENGTH(q.answer)), CHAR_LENGTH(q.answer) ' \
                     'FROM SQUAD_KO_WIKI.all_qna AS q INNER JOIN SQUAD_KO_WIKI.all_context_ori AS c ON q.c_id = c.id'
        """
        select_sql =' SELECT c.id,c.title,c.context,q.q_id,q.question,q.answer, CHAR_LENGTH(q.answer) ' \
                    'FROM SQUAD_KO_ORI.all_qna AS q ' \
                    'INNER JOIN SQUAD_KO_ORI.all_context_ori AS c ' \
                    'ON q.c_id = c.id ' \
                    'WHERE SUBSTRING_INDEX(q.q_id, "_", 1) = 1 ' \
                    'OR SUBSTRING_INDEX(q.q_id, "_", 1) = 3 ' \
                    'OR SUBSTRING_INDEX(q.q_id, "_", 1) = 4 ' \
                    'OR SUBSTRING_INDEX(q.q_id, "_", 1) = 5 order by abs(id)'
        self.cur.execute(select_sql)
        print(datetime.datetime.now(), "1")

        select_data = self.cur.fetchall()
        """
        for sd in select_data:
            if "-1" in sd[3]:
                for s in sd:
                    self.f2.write(str(s))
                    self.f2.write("\t")
                q_id = sd[3].replace("-1","-2")
                for sdsd in select_data:
                    if "-2" in sdsd[4] and sdsd[3] in q_id:
                        self.f2.write(str(sdsd[3]))
                        self.f2.write("\t")
                        self.f2.write(str(sdsd[4]))
                        self.f2.write("\n")
                        self.f2.flush()
                    # else:
                        # self.f2.write("\n")
        print(datetime.datetime.now(), "1")
        """
        select_data1 = []
        select_data2 = []
        for sd in select_data:
            if "-1" in sd[3]:
                select_data1.append(sd)
            elif "-2" in sd[3]:
                select_data2.append(sd)

        for s1 in select_data1:
            for s in s1:
                self.f2.write(str(s).replace("\t"," "))
                self.f2.write("\t")
            q_id = s1[3].replace("-1","-2")
            c_id = s1[0]
            for s2 in select_data2:
                if s2[3] in q_id and s2[0] in c_id:
                    self.f2.write(str(s2[3]))
                    self.f2.write("\t")
                    self.f2.write(str(s2[4]))
            self.f2.write("\n")
            self.f2.flush()

        print(datetime.datetime.now(), "2")


    def select_data3(self):
        print (datetime.datetime.now(), 'select start')
        """
        select_sql ='SELECT c.id, c.title, c.context as context_ori, cc.context as context_con, q.q_id, q.question, q.answer, q.answer_start, CHAR_LENGTH(q.answer) ' \
                    'FROM SQUAD_KO_ORI.all_qna AS q INNER JOIN SQUAD_KO_ORI.all_context_ori AS c ON q.c_id = c.id INNER JOIN SQUAD_KO_ORI.all_context AS cc ON q.c_id = cc.id ' \
                    'WHERE SUBSTRING_INDEX(q.q_id, "_", 1) = 1 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 3 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 4 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 5 ORDER BY ABS(c.id)'
        """
        select_sql ='SELECT c.id, c.title, c.context as context_ori, cc.context as context_con, q.q_id, q.question, q.answer, q.answer_start, CHAR_LENGTH(q.answer) ' \
                    'FROM SQUAD_KO_ORI.all_qna AS q INNER JOIN SQUAD_KO_ORI.all_context_ori AS c ON q.c_id = c.id INNER JOIN SQUAD_KO_ORI.all_context AS cc ON q.c_id = cc.id ' \
                    'WHERE SUBSTRING_INDEX(q.q_id, "_", 1) = 3 ORDER BY ABS(c.id)'
        self.cur.execute(select_sql)
        print(datetime.datetime.now(), "1")

        select_data = self.cur.fetchall()
        select_data1 = []
        select_data2 = []
        for sd in select_data:
            if "-1" in sd[4]:
                select_data1.append(sd)
            elif "-2" in sd[4]:
                select_data2.append(sd)

        for s1 in select_data1:
            rm_ori = s1[2].replace("|"*5, "").replace("$"*5, "").replace("@"*5, "")
            context_start = rm_ori.find(str(s1[3]))

            for s in s1:
                self.f2.write(str(s))
                self.f2.write("\t")
            self.f2.write(str(rm_ori))
            self.f2.write("\t")
            self.f2.write(str(context_start))
            self.f2.write("\t")
            if context_start != -1:
                self.f2.write(rm_ori[int(s1[7])+int(context_start): int(s1[7])+int(context_start)+int(s1[8])])
                self.f2.write("\t")
            else:
                self.f2.write("null")
                self.f2.write("\t")

            self.f2.write("\t")

            q_id = s1[4].replace("-1", "-2")
            c_id = s1[0]
            for s2 in select_data2:
                if s2[4] in q_id and s2[0] in c_id:
                    self.f2.write(str(s2[4]))
                    self.f2.write("\t")
                    self.f2.write(str(s2[5]))
            self.f2.write("\n")
            self.f2.flush()
        print(datetime.datetime.now(), "2")

    def select_data4(self):
        print (datetime.datetime.now(), 'select start')
        select_sql ='SELECT c.id, c.title, c.context as context_ori, cc.context as context_con, q.q_id, q.question, q.answer, q.answer_start, CHAR_LENGTH(q.answer) ' \
                    'FROM SQUAD_KO_ORI.all_qna AS q INNER JOIN SQUAD_KO_ORI.all_context_ori AS c ON q.c_id = c.id INNER JOIN SQUAD_KO_ORI.all_context AS cc ON q.c_id = cc.id ' \
                    'WHERE SUBSTRING_INDEX(q.q_id, "_", 1) = 1 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 3 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 4 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 5 OR SUBSTRING_INDEX(q.q_id, "_", 1) = 18 ' \
                    'ORDER BY ABS(c.id)'
        self.cur.execute(select_sql)
        print(datetime.datetime.now(), "1")

        select_data = self.cur.fetchall()
        select_data1 = []
        select_data2 = []

        for sd in select_data:
            if "-1" in sd[4]:
                select_data1.append(sd)
            elif "-2" in sd[4]:
                select_data2.append(sd)
        temp_list = [[] for _ in range(len(select_data1))]
        print (len(select_data1))

        for s1, i in zip(select_data1, range(len(select_data1))):
            rm_ori = s1[2].replace("|"*5, "").replace("$"*5, "").replace("@"*5, "")
            context_start = rm_ori.find(str(s1[3]))

            for s in s1:
                temp_list[i].append(s)
            temp_list[i].append(rm_ori)
            temp_list[i].append(context_start)
            if context_start != -1:
                temp_list[i].append(rm_ori[int(s1[7])+int(context_start): int(s1[7])+int(context_start)+int(s1[8])])
            else:
                temp_list[i].append("null")

            q_id = s1[4].replace("-1", "-2")
            c_id = s1[0]
            for s2 in select_data2:
                if s2[4] in q_id and s2[0] in c_id:
                    temp_list[i].append(str(s2[4]))
                    temp_list[i].append(str(s2[5]))
        for t_list in temp_list:
            for t in t_list:
                self.f2.write("".join(str(t)))
                self.f2.write("\t")
            self.f2.write("\n")
        print(datetime.datetime.now(), "2")

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
    j.select_data4()
    # j.count_data()
    # logger.info("All finished")