import os, sys
import pymysql
import logging
import ys.cute.sams.ys_logger as ys_logger
import concurrent.futures

sys.path.append(os.path.abspath('..'))

logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(ys_logger.MyHandler())
logger.info("Finish setting logger")


class SquadDb():

    def __init__(self):
        self.db_cnf_dict = {"host": '10.122.64.71', "usr": "root", "pwd": "root",
                            "db": "cmdb", "encoding": "utf8"}
        self.con = None
        self.cur = None
        self.connect_db()
        # self.f2 = open("not_dup.txt", "w", newline="\n")
        # self.f3 = open("/home/msl/ys/cute/sams/tmp/180824_17년11월1일이후기사랜덤3만개(다씀)_id만.txt","r")
        self.q_id_1 = ""
        self.q_id_2 = ""
        self.question_1 = ""
        self.question_2 = ""
        self.result_list = []
        self.test = False

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

    def compare(self):
        logger.info("Start Selection")
        if self.test is True:
            select_sql = 'select REG_DATE, TITLE, CONTENT, ID from NEWS ' \
                        'where ID != "" AND TITLE !="" AND CONTENT !="" AND URL !="" AND AUTHOR !="" AND COMMENTS !="" AND CREATE_DATE !="" AND REG_DATE !="" ' \
                        'AND DATE > 20171101000000 ' \
                        'AND CATEGORY = "연예"' \
                        'order by rand() limit 100'
        else:
            select_sql ='select REG_DATE, TITLE, CONTENT, ID from NEWS ' \
                        'where ID != "" AND TITLE !="" AND CONTENT !="" AND URL !="" AND AUTHOR !="" AND COMMENTS !="" AND CREATE_DATE !="" AND REG_DATE !="" ' \
                        'AND DATE > 20171101000000 ' \
                        'AND CATEGORY = "연예"' \
                        'order by rand() limit 30000'
        self.cur.execute(select_sql)
        logger.info("Selected")

        select_data = self.cur.fetchall()
        logger.info(len(select_data))
        data = self.f3.readlines()

        for sd in select_data:
            reg_date = sd[0]
            print (reg_date)
            id = sd[3]
            flag = True

            for d in data:
                item = d.split("\t")
                if item[0] == reg_date and item[1] == id:
                    flag = False
                    break
            if flag:
                print (sd)
                self.f2.write("\t".join([sd[0], sd[1], sd[2], sd[3]]))

        self.f2.close()
        self.f3.close()
        logger.info("Finish")

    def compare2(self):
        logger.info("Start Selection")
        if self.test is True:
            select_sql = 'select REG_DATE, TITLE, CONTENT, ID from NEWS ' \
                        'where ID != "" AND TITLE !="" AND CONTENT !="" AND URL !="" AND AUTHOR !="" AND COMMENTS !="" AND CREATE_DATE !="" AND REG_DATE !="" ' \
                        'AND DATE > 20171101000000 ' \
                        'AND CATEGORY = "연예"' \
                        'order by rand() limit 100'
        else:
            select_sql ='select REG_DATE, TITLE, CONTENT, ID from NEWS ' \
                        'where ID != "" AND TITLE !="" AND CONTENT !="" AND URL !="" AND AUTHOR !="" AND COMMENTS !="" AND CREATE_DATE !="" AND REG_DATE !="" ' \
                        'AND DATE > 20171101000000 ' \
                        'AND CATEGORY = "연예"' \
                        'order by rand() limit 100000'
        self.cur.execute(select_sql)
        logger.info("Selected")

        select_data = self.cur.fetchall()
        logger.info(len(select_data))
        workers = 10
        r = 500

        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as exe:
            fs = {exe.submit(comp, select_data, n, r) for n in range(0, len(select_data), r)}



        logger.info("Finish")

    def count_data(self):
        logger.info("count start")
        try:
            count_sql = 'select count(*) from NEWS'
            self.cur.execute(count_sql)
            select_count_row = self.cur.fetchall()
            logger.info(select_count_row)
            self.con.commit()

        except:
            logger.info("cannnot user_information")

f3 = open("/home/msl/ys/cute/sams/tmp/180824_17년11월1일이후기사랜덤3만개(다씀)_id만.txt","r")
data = f3.readlines()
f2 = open("not_dup.txt", "w", newline="\n")
def comp(select_data, n, r):
    logger.info("processing: {} ..< {}".format(n, n + r))
    for sd in select_data[n:n + r]:
        reg_date = sd[0]
        id = sd[3]
        flag = True

        for d in data:
            item = d.split("\t")
            if item[0] == reg_date and item[1] == id:
                flag = False
                break
        if flag:
            # print(sd)
            if len(sd) == 4 and 300 <= len(sd[2]) <= 3000:
                f2.write("\t".join([sd[0], sd[1], sd[2], sd[3]]))
                f2.write("\n")


if __name__ == "__main__":
    j = SquadDb()
    # j.connect_db()
    j.compare2()
    f2.close()
    f3.close()