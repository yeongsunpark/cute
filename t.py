# -*- coding: utf-8 -*-

import sys
import logging
sys.path.append("/home/msl/ys/git/linguistic-lab/mrc_utils/json2db")

import custom_logger
from morp_analyze_my import NLPAnalyzer


def return_myself(token):
    return token

logger = logging.getLogger('root')
logger.setLevel("DEBUG")
logger.addHandler(custom_logger.MyHandler())
logger.info("Finish setting logger")

"""
input_list = [[['이것/np', 'ㄴ/jx'], ['정답/nng', '이/vcp', '다/ec']]] # [[['정답/nng']]]
return_list = list()
depth = 0
for x in input_list:  # x: sentence
    for y in x:  # y: token
        if type(y) != list:
            return_list.append(y)
            depth = 2
        else:
            for z in y:  # z: morph
                return_list.append(z)
                print (type(z))
                depth = 3
print(return_list, depth)
# ['이것/np', 'ㄴ/jx', '정답/nng', '이/vcp', '다/ec'] 3
# ['정답/nng'] 3

print (['|/sw'] * 5 + return_list + ['|/sw'] * 5)

temp_list = [(1, 6) for _ in range(len(input_list)+5)]
print (temp_list)
"""

def extract_passage(ctx, answer, location, c_id, q_id):
    sentence_list = list()
    is_skip = False
    logger.info(answer)
    processed_ans = [[['정답/nng']]]  # list
    # [[['이것/np', 'ㄴ/jx'], ['정답/nng', '이/vcp', '다/ec']]] # [[['정답/nng']]]
    logger.debug(processed_ans)
    processed_ans_plain = ['정답/nng']
    depth = 3
    processed_ans_plain = ['|/sw'] * 5 + processed_ans_plain + ['|/sw'] * 5  # plain list
    logger.debug("processed_ans: {}".format(processed_ans))
    logger.debug("processed_ans_plain: {}".format(processed_ans_plain))
    ctx = "{}{}{}{}{}".format(ctx[:location], "|" * 5, ctx[location:location + len(answer)], "|" * 5,
                              ctx[location + len(answer):])
    logger.debug("*****ctx*****: {}".format(ctx))
    processed_txt = [[['이것/np', 'ㄴ/jx'], ['정답/nng', '이/vcp', '다/ec']]]
    sentence_list = True
    logger.debug(processed_txt)
    # processed_txt_plain = ['이것/np', 'ㄴ/jx', '정답/nng', '이/vcp', '다/ec']
    processed_txt_plain = ['이것/np', 'ㄴ/jx', '|/sw', '|/sw', '|/sw', '|/sw', '|/sw', '정답/nng', '|/sw', '|/sw', '|/sw', '|/sw', '|/sw', '이/vcp', '다/ec']
    depth = 3

    logger.debug("processed_ans: {}".format(processed_ans))
    logger.debug("processed_ans_plain: {}".format(processed_ans_plain))
    logger.debug("processed_txt: {}".format(processed_txt))
    logger.debug("processed_txt_plain: {}".format(processed_txt_plain))
    marker_idxes = [(j, j + 5) for j in range(len(processed_txt_plain))
                    if processed_txt_plain[j:j + 5] == ['|/sw'] * 5]
    logger.debug("*****marker_idxes***** {}".format(marker_idxes))
    if len(marker_idxes) % 2 == 0:
        logger.debug("*****len(marker_idxes)***** {}".format(len(marker_idxes)%2))
        if len(marker_idxes) == 2:
            start_idx = marker_idxes[0][0]  # 2(정)
            end_idx = marker_idxes[1][1] - 10  # 3(답)
        else:
            logger.critical("Not 2 markers...({}) skip: {}".format(len(marker_idxes), q_id))
            is_skip = True
            return 0, 0, 0, 0, is_skip
    else:
        logger.critical("Not 2 markers...({}) skip: {}".format(len(marker_idxes), q_id))
        is_skip = True
        return 0, 0, 0, 0, is_skip

    logger.debug("start_idx: {}".format(start_idx))
    logger.debug("end_idx: {}".format(end_idx))

    for k in range(len(processed_txt)):  # sentence
        for l in range(len(processed_txt[k])):  # token
            logger.debug(processed_txt[k][l])
            tmp_idxes = [(j, j + 5) for j in range(len(processed_txt[k][l]))
                         if processed_txt[k][l][j:j + 5] == ['|/sw'] * 5]
            if len(tmp_idxes) != 0:
                logger.debug(tmp_idxes)
                new_processed_txt = remove_list_sequence(processed_txt[k][l], tmp_idxes)
                logger.debug(new_processed_txt)
                processed_txt[k][l] = new_processed_txt
                # processed_txt[k][l] = list(filter('|/sw'.__ne__, processed_txt[k][l]))
                logger.debug(processed_txt[k][l])
    logger.debug("processed_txt: {}".format(processed_txt))
    final_answer = list()
    cnt = 0

    for k in range(len(processed_txt)):
        tmp = list()
        for l in range(len(processed_txt[k])):
            tmp2 = list()
            for m in range(len(processed_txt[k][l])):  # morph
                if cnt >= start_idx and cnt < end_idx:
                    logger.debug(processed_txt[k][l][m])
                    tmp2.append(processed_txt[k][l][m])
                cnt += 1
            if len(tmp2) > 0:
                tmp.append(tmp2)
        if len(tmp) > 0:
            final_answer.append(tmp)
        logger.debug("***************final_answer{}".format(final_answer))
    processed_txt_plain = remove_list_sequence(processed_txt_plain, marker_idxes)
    logger.debug("%^%^%^processed_txt_plain{}".format(processed_txt_plain))  # ['이것/np', 'ㄴ/jx', '정답/nng', '이/vcp', '다/ec']
    # processed_txt_plain = list(filter('|/sw'.__ne__, processed_txt_plain))
    final_answer_plain, depth = make_plain_list(final_answer)
    logger.debug("%^%^%^final_answer_plan{}".format(final_answer_plain))  # ['정답/nng'], 3
    try:
        assert (processed_txt_plain[start_idx:end_idx] == final_answer_plain)
    except AssertionError:
        logger.error("{} != {}".format(processed_txt_plain[start_idx:end_idx],
                                       final_answer_plain))
        is_skip = True
        return 0, 0, 0, 0, is_skip
    logger.debug("answer_processed: {}".format(processed_txt_plain[start_idx:end_idx]))
    logger.debug("answer_processed_return: {}".format(final_answer))
    logger.debug(str(processed_txt))
    return start_idx, end_idx, str(processed_txt), str(final_answer), is_skip, sentence_list


def remove_list_sequence(input_list, marker_idxes):
        # ['이것/np', 'ㄴ/jx', '|/sw', '|/sw', '|/sw', '|/sw', '|/sw', '정답/nng', '|/sw', '|/sw', '|/sw', '|/sw', '|/sw', '이/vcp', '다/ec']
        # [(2, 7), (8, 13)]
        logger.debug(input_list)
        logger.debug(marker_idxes)
        new_ptp = list()
        if len(marker_idxes) > 1:
            for i in range(len(marker_idxes)):
                if i == 0:
                    new_ptp += input_list[:marker_idxes[i][0]]
                    # '이것/np', 'ㄴ/jx'
                    new_ptp += input_list[marker_idxes[i][1]:marker_idxes[i + 1][0]]
                    # 정답/nng'
                    logger.debug(input_list[:marker_idxes[i][0]])
                else:
                    new_ptp += input_list[marker_idxes[i][1]:]
                    # '이/vcp', '다/ec'
                    logger.debug(input_list[marker_idxes[i][1]:])
        else:
            new_ptp += input_list[:marker_idxes[0][0]]
            new_ptp += input_list[marker_idxes[0][1]:]
        logger.debug(new_ptp)
        # ['이것/np', 'ㄴ/jx', '정답/nng', '이/vcp', '다/ec']
        return new_ptp

def make_plain_list(input_list):  #[[['정답/nng']]]
        return_list = list()
        depth = 0
        for x in input_list:    # x: sentence
            for y in x:     # y: token
                if type(y) != list:
                    return_list.append(y)
                    depth = 2
                else:
                    for z in y:     # z: morph
                        return_list.append(z)
                        depth = 3
        return return_list, depth
        # ['정답/nng'], 3

if __name__ == "__main__":
    # def extract_passage(self, ctx, answer, location, c_id, q_id):
    print(extract_passage("이것은 정답이다", "정답", 4, "1", "2-3"))