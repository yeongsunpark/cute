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
        self.f2 = open("c_change.txt", "w", newline="\n")
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

    def change(self):
        logger.info("Start Selection")
        if self.test is True:
            select_sql = 'select REG_DATE, TITLE, CONTENT, CATEGORY, ID from NEWS '\
                         'where REG_DATE >20180000000000 AND CATEGORY != "연예" '\
                         'order by rand() limit 10'
        else:
            select_sql ='select REG_DATE, TITLE, CONTENT, CATEGORY, ID from NEWS '\
                         'where REG_DATE >20180000000000 AND CATEGORY != "연예" '\
                         'order by rand() limit 20000'
        self.cur.execute(select_sql)
        logger.info("Selected")

        select_data = self.cur.fetchall()
        logger.info(len(select_data))

        economy = ["금융기타", "대출", "증권", "취업"]
        science = ["IT기타", "게임", "과학기타", "날씨", "모바일", "비만성장", "생활가전", "성형외과", "소프트웨어", "수송기기", "영상음향가전", "의료기타", "자동차",
                   "제약", "피부과", "하드웨어", "항공"]
        society = ["결혼", "교육", "사회기타", "생활용품", "육아", "종교"]
        sports = ["경마", "골프", "동계스포츠", "레저스포츠", "스포츠기타", "야구", "축구"]
        normal = ["국방", "기호식품", "복권", "부동산", "쇼핑", "숙박", "식품기타", "애완", "여행기타", "연금보험", "인테리어", "재해", "정치", "탈모", "패션",
                  "화장품", "공연", "영화", "예술"]


        for sd in select_data:
            cate = sd[3]
            if cate in economy:
                c = "경제"
            elif cate in science:
                c = "과학"
            elif cate in society:
                c = "사회"
            elif cate in sports:
                c = "스포츠"
            elif cate in normal:
                c = "일반"
            elif cate == "":
                c = "null"
            else:
                c = "error"
            # print (sd)
            if 300 <= len(sd[2]) <= 3000:
                self.f2.write("\t".join([sd[0], sd[1], sd[2], c, sd[4]]))
                self.f2.write("\n")
        self.f2.close()
        # self.f3.close()
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

def split():
    c = dict()
    science = []
    society = []
    sports = []
    general = []
    economy = []
    etc = []

    f2 = open("c_change.txt", "r")
    for line1 in f2:
        item = line1.split("\t")
        if len(item) == 5:
            category = item[3]

            if category == "과학":
                science.append(line1)
            elif category == "사회":
                society.append(line1)
            elif category == "스포츠":
                sports.append(line1)
            elif category == "일반":
                general.append(line1)
            elif category == "경제":
                economy.append(line1)
            else:
                etc.append(line1)
        category_list = [science, society, sports, general, economy, etc]
    str_category_list = ["science", "society", "sports", "general", "economy", "etc"]

    for cl1, cl2 in zip(category_list, str_category_list):
        with open("{}.txt".format(cl2), "w") as f3:
            for l in cl1:
                item = l.split("\t")
                # c_id, title, context(marker), q_id_1, question_1, q_id_2, question_2, answer
                f3.write(l)
                # f3.write("\n")







if __name__ == "__main__":
    # j = SquadDb()
    # j.connect_db()
    # j.change()
    split()