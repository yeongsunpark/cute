#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import re

sys.path.insert(0,'..')

input_dir = "/home/msl/ys/cute/data"
output_dir = "/home/msl/ys/cute/output"

aa = re.compile('제\d+장')  #
bb = re.compile('제\d+절')  #
cc = re.compile('제\d+조')  #
dd = re.compile('부칙')
# 하기 전에 txt 파일이 utf-8로 인코딩이 되어 있나 꼭 확인하기!
# utf-8 파일은 제일 윗 줄을 제대로 인식을 못하니 한 줄 띄기!


# 인덱스를 무시하기 위한 용도로 언더스코어(_)가 사용 되었다.
# [[for i in range(2)] for j in range(6)] 보통 이렇게 쓰는데 i, j 를 안 쓸 거 같아서 언더스코어(_)를 적어주었다.

previous_lvl = -1
current_lvl = -1
content_flag = False




for f in os.listdir(input_dir):
    with open(os.path.join(input_dir, f), "r") as f:
    # with open("test.txt", "r") as f:
        data = []
        temp_datas = [['' for _ in range(2)] for _ in range(3)]
        for line in f:
            line = line.replace("\n", "<br>")
            if aa.match(line) or dd.match(line):
                current_lvl = 0
            elif bb.match(line):
                current_lvl = 1
            elif cc.match(line):
                current_lvl = 2
            else:
                content_flag = True

            if content_flag:  # 내용 부분에 관한 내용입니다.
                if temp_datas[current_lvl][1] == '':
                    temp_datas[current_lvl][1] = line  # 내용이 없다면 temp_datas[current_lvl]의 두번째에 내용을 집어 넣는다.
                else:
                    temp_datas[current_lvl][1] += ' ' + line  # 이미 내용이 적혀 있으니 스페이스 하나 하고 붙여 넣기한다.
            else:
                temp_datas[current_lvl][1] = line

            if (content_flag or previous_lvl < current_lvl) and len(
                    data) > 0:  # 만약에 content_flag가 맞거나 previous_lvl이 current_lvl보다 작고 data가  0 보다 크면.
                # print "data0", data[0]
                # print "data-1", data[-1]
                del data[-1]  # data[-1]을 지우는데... 이걸 안 지우면 뭔가 많아짐 ㅋㅋ 왜 많아지는지는 차근차근 알아가보자.
                # del data[-1]  # data[-1] data.append 할 때마다 한 줄씩 추가가 되는데 그 때 완벽하지 않은 문장이 추가 될 때가 있음. 내가 완벽한 문장이면 그 전 문장(완벽하지 않은 문장)을 지워주는 역할이다.

            elif previous_lvl > current_lvl:  # previous_lvl 이 현재 lvl 보다 크면 새로 시작해야지!
                for i in range(current_lvl + 1, 3):
                    # print (temp_datas[i][0], ":", temp_datas[i][1])
                    temp_datas[i] = ['', '']  # 이건 또 뭘까. 근데 이걸 안 쓰면 내용이 있어야 하는 부분에 내용이 없는 문장이 만들어짐.
                    # temp_datas[i] = ['', ''] 새로 시작하게 될 때 이걸 안 쓰면 위에 있는 내용이 남아 있음. 지워주는 역할을 한다.
            data.append('\t'.join(['\t'.join(temp_data) for temp_data in temp_datas]))
            previous_lvl = current_lvl
            content_flag = False
    with open(os.path.join(output_dir, "result_{}".format(f.name.split("/")[-1])), "w", encoding='utf8') as f2:
        # with open(os.path.join(input_dir, "result_1.txt"), "w", encoding='utf8') as f2:
        print (f.name.split("/")[-1])
        f2.write('\n'.join(data))