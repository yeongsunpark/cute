import os, sys
import pymysql
import logging
import ys_logger
import work_sql_ut as yu
import re
import json

sys.path.append(os.path.abspath('..'))

logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.83', "usr": "root", "pwd": "data~secret!",
                            "db": "SQUAD_KO_WIKI", "encoding": "utf8"}
        self.con = None
        self.cur = None
        self.connect_db()
        # self.f = open("select4.txt", "w", newline="")
        self.json_data = open("work_sql.json","r")
        self.d = self.json_data.read()
        self.d = json.loads(self.d)
        self.f = open(self.d['TEST']['f'], "w", newline="")
        self.q_id_1 = ""
        self.q_id_2 = ""
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
        try:  # try to connect to project db
            cfg_dict = dict(host=self.db_cnf_dict['host'], usr=self.db_cnf_dict['usr'],
                            pwd=self.db_cnf_dict['pwd'], db=self.db_cnf_dict['db'])
            self.easy_mysql(cfg_dict, encoding=self.db_cnf_dict['encoding'],
                            autocommit=True)  # turn-on autocummit, be careful!
            self.cur.execute("SET NAMES utf8")
        except Exception as e:
            pass

    def select_data4(self):
        self.f.write("\t".join(["c_id", "title", "context_ori", "context_con", "q_id-1", "q-1", "answer", "q_start", "len_answer", "rm_context", "con_start", "ex_answer",
                                 "q_id-2", "q-2", "m_context", "m_ex_answer", "\n"]))
        logger.info("Start Selection")

        select_sql = self.d['TEST']['QUERY']

        self.cur.execute(select_sql)

        logger.info("Selected")
        select_data = self.cur.fetchall()
        select_data1 = []
        select_data2 = []

        for sd in select_data:
            if "-1" in sd[4]:  # q.q_id
                select_data1.append(sd)
            elif "-2" in sd[4]: # q.q_id
                select_data2.append(sd)
        temp_list = [[] for _ in range(len(select_data1))]
        logger.info(len(select_data1))

        for s1, i in zip(select_data1, range(len(select_data1))):
            rm_ori = s1[2].replace("|"*5, "").replace("$"*5, "").replace("@"*5, "").replace("|"*3,"").replace("$"*3,"").replace("@"*3,"")  # c.context as context_ori
            context_start = rm_ori.find(str(s1[3]))  # cc.context as context_con (short version context)

            for s in s1:
                temp_list[i].append(s)
            temp_list[i].append(rm_ori)
            temp_list[i].append(context_start)
            if context_start != -1:
                extract_answer = rm_ori[int(s1[7])+int(context_start): int(s1[7])+int(context_start)+int(s1[8])]
                temp_list[i].append(rm_ori[int(s1[7])+int(context_start): int(s1[7])+int(context_start)+int(s1[8])])  # extract_answer

            else:
                temp_list[i].append("null")

            q_id = s1[4].replace("-1", "-2")
            c_id = s1[0]
            for s2 in select_data2:
                if s2[4] in q_id and s2[0] in c_id:
                    temp_list[i].append(str(s2[4]))
                    temp_list[i].append(str(s2[5]))
        for t_list in temp_list:
            # if len(t_list) ==14:
            if len(t_list) ==14:
                if t_list[6] == t_list[11] and t_list[12] !="":
                    m_context = yu.insert_str(string=t_list[9], s_index=int(t_list[7])+int(t_list[10]), e_index=int(t_list[7]+int(t_list[8])+int(t_list[10])))
                    t_list.append(m_context)
                    a = yu.regu(m_context)
                    t_list.append(a)
                    if t_list[6] == t_list[11] == a:
                        al = "all same"
                    else:
                        al = "diff"
                    t_list.append(al)

                    for t in t_list:
                        self.f.write("".join(str(t)))
                        self.f.write("\t")
                    self.f.write("\n")
            elif len (t_list) == 12:
                    t_list.append("")
                    t_list.append("")
                    m_context = yu.insert_str(string=t_list[9], s_index=int(t_list[7]) + int(t_list[10]),
                                              e_index=int(t_list[7] + int(t_list[8]) + int(t_list[10])))
                    t_list.append(m_context)
                    a = yu.regu(m_context)
                    t_list.append(a)
                    # if t_list[6] == t_list[11] == a:
                    # al = "all same"
                    # else:
                    # al = "diff"
                    t_list.append(al)

                    for t in t_list:
                        self.f.write("".join(str(t)))
                        self.f.write("\t")
                    self.f.write("\n")


        logger.info("Finish")


    def count_data(self):
        logger.info("count start")
        try:
            count_sql = 'select count(*) from SQUAD_KO_WIKI.all_qna'
            self.cur.execute(count_sql)
            select_count_row = self.cur.fetchall()
            logger.info(select_count_row)
            self.con.commit()

        except:
            logger.info("cannnot user_information")


if __name__ == "__main__":
    j = SquadDb()
    # j.connect_db()
    j.select_data4()