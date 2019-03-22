author__ = "Lynn Hong"
__date__ = "06/08/2017"

import json
import logging
import os, sys
import random
import math
import time
import re
import concurrent.futures
import string
from multiprocessing import Pool

import pymysql

sys.path.append(os.path.abspath('..'))
import custom_logger


def return_myself(token):
    return token

logger = logging.getLogger('root')
logger.setLevel("INFO")
logger.addHandler(custom_logger.MyHandler())
logger.info("Finish setting logger")

class SquadDb():

    def __init__(self):
        ###user_input#########################################################
        self.db_table = "SQUAD_KO_WIKI"
        self.data_output_dir = "/home/msl/ys/cute/mobis/data"
        self.lang = "mobis"
        self.version = "1"
        self.test_ratio = 0.1    # dev_ratio
        self.maximum = None
        self.is_dp = False
        self.is_random = True
        self.is_fixed = False
        #######################################################################


        self.con = None
        self.cur = None
        self.random_end = "ORDER BY RAND()" if self.is_random else ""
        self.dp_end = "_dp" if self.is_dp else ""
        self.context_ori = ""

    def easy_mysql(self, cfg_dict, encoding='utf8', autocommit=False):
        self.con = pymysql.connect(host=cfg_dict['host'], user=cfg_dict['usr'],
                                   passwd=cfg_dict['pwd'], db=cfg_dict['db'], charset=encoding)
        self.cur = self.con.cursor()
        if autocommit is True:
            self.con.autocommit(True)

    def connect_db(self, table_name):
        try:        # try to connect to project db
            cfg_dict = dict(host='localhost', usr= 'root', pwd='data~secret!', db=table_name)
            self.easy_mysql(cfg_dict, encoding='utf8', autocommit=True)
            self.cur.execute("SET NAMES utf8")
        except Exception as e:
            logger.critical(e)
        logger.info("Finish connecting to database...")

    def db2squad(self):
        if self.maximum is not None:
            #fetch_sql_ctx = "SELECT id, title, context, context_morph, context_dp FROM all_context_all WHERE season !=2 and season !=10 {} LIMIT {};"\
            fetch_sql_ctx = "SELECT id, title, context FROM all_context_all {} LIMIT {};"\
                .format(self.random_end, self.maximum)
        else:
            fetch_sql_ctx = "SELECT id, title, context FROM all_context_all {};"\
                 .format(self.random_end)
            # fetch_sql_ctx = "SELECT id, title, context, context_morph, context_dp FROM all_context_all where season = 2 or season = 7 or season = 8 or season = 9 or season = 10 or season = 13 {};"\
                #.format(self.random_end)
        self.cur.execute(fetch_sql_ctx)
        contexts = self.cur.fetchall()   # entire
        if self.is_fixed:
            self.cur.execute("SELECT id, title, context FROM dev_context_fix {};"
                             .format(self.random_end))
            contexts_dev_fix = self.cur.fetchall()  # dev_fix
        else:
            contexts_dev_fix = []  # dev_fix
        contexts_dev_fix_ids = [row[0] for row in contexts_dev_fix]
        contexts_not_fix = [c for c in contexts if c[0] not in contexts_dev_fix_ids]  # not fix
        logger.info("len(contexts): {}".format(len(contexts)))
        logger.info("len(contexts_dev_fix_ids): {}".format(len(contexts_dev_fix_ids)))
        logger.info("len(contexts_not_fix): {}".format(len(contexts_not_fix)))

        train_cnt = math.floor((len(contexts))*(1-self.test_ratio))
        context_train = random.sample(contexts_not_fix, train_cnt)
        c_dev_tmp1 = [c for c in contexts_not_fix if c not in context_train]
        c_dev_tmp2 = list(contexts_dev_fix)
        logger.info("c_dev_tmp1: {}".format(len(c_dev_tmp1)))
        logger.info("c_dev_tmp2: {}".format(len(c_dev_tmp2)))
        context_dev = c_dev_tmp1 + c_dev_tmp2
        logger.info("train_cnt: {}".format(train_cnt))
        logger.info("Len context_train: {}".format(len(context_train)))
        logger.info("Len context_dev: {}".format(len(context_dev)))

        for data_type in ["train", "dev"]:
            cnt = 0
            result = dict()
            result['version'] = self.version
            result['creator'] = "MINDs Lab."
            result['data'] = list()
            logger.info("Data type {} start..".format(data_type))
            for context in eval("context_{}".format(data_type)):
                data_dict = dict()      # each context
                data_dict['title'] = context[1]
                data_dict['paragraphs'] = list()
                para_dict = dict()
                # para_dict['context_original'] = context[2]
                para_dict['context'] = context[2]
                if self.is_dp:
                    para_dict['dp'] = context[4]
                # try:
                    # para_dict['context'] = context[3]
                # except IndexError:
                    # logger.critical(context)
                    # exit()
                qas_list = list()
                if self.lang == "kor":
                    fetch_sql_qa = "SELECT q_id, question, answer_start_morph, answer_end_morph, answer_morph, " \
                                   "question_morph, answer, question_dp " \
                                   "FROM all_qna WHERE c_id='{}'".\
                        format(context[0])
                else:
                    fetch_sql_qa = "SELECT q_id, question, answer_start, answer FROM all_qna " \
                                   "WHERE c_id='{}'".format(context[0])
                self.cur.execute(fetch_sql_qa)
                for row in self.cur.fetchall():
                    if self.lang == "kor":
                        qa = {'id': row[0],
                              'answers': [{'answer_start': row[2], 'answer_end': row[3],
                                           'text': row[4], 'text_original': row[6]}],
                              'question_original': row[1], 'question': row[5]}
                        if self.is_dp:
                            qa['question_dp'] = row[7]
                    else:
                        qa = {'id': row[0], 'answers': [{'answer_start': row[2], 'text': row[3], 'answer_end': row[2]+len(row[3])}],
                              'question': row[1]}
                    qas_list.append(qa)
                    cnt += 1
                para_dict['qas'] = qas_list
                data_dict['paragraphs'].append(para_dict)
                result['data'].append(data_dict)
            logger.info("Finish creating json structure({})".format(data_type))
            with open(os.path.join(self.data_output_dir, "ko_law_v{}_squad{}_{}.json".
                    format(self.version, self.dp_end, data_type)),
                      'w', encoding='utf8') as fp:
                json.dump(result, fp, ensure_ascii=False)
            with open(os.path.join(self.data_output_dir, "ko_law_v{}_squad_pretty{}_{}.json".
                    format(self.version, self.dp_end, data_type)),
                      'w', encoding='utf8') as fp:
                json.dump(result, fp, ensure_ascii=False, indent=2)
            logger.info("Data dump {} finished..: len {}".format(data_type, cnt))

if __name__ == "__main__":

    j = SquadDb()
    j.connect_db(j.db_table)
    j.db2squad()
    logger.info("All finished")
