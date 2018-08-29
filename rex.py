

"""
def insert_str(string, str_to_insert, s_index, e_index):
    # return string[:index] + str_to_insert + string[index:]
    return string[:s_index] + str_to_insert + string[s_index:e_index] +  str_to_insert + string[e_index:]

f = open ("data/wa.txt", "r")
f2 = open ("data/wa_res.txt", "w")

for line in f:
    item = line.strip().split("\t")
    s_index = int(item[0].replace(u"\ufeff", ''))
    answer = item[6]
    context = item[7]
    e_index = s_index + len(answer)
    str_to_insert = "|||||"

    data = insert_str(context, str_to_insert, s_index, e_index)

    f2.write(data)
    f2.write("\n")
"""
import re
import csv

def rex_str(para):
    m = re.search('\|\|\|\|\|(.*?)\|\|\|\|\|', para)
    # m = re.search('\[Image\](.*?)\[\/Image\]', str(para))
    return m.group(1)


f = open("/home/msl/data/mrc/ko_kakao/전달용-1(c71까지)(14828)_수정(k2) - 시트1의 사본.tsv", "r")
# f2 = open("/home/msl/data/mrc/ko_kakao/result.tsv", "w")
f2 = open("/home/msl/data/mrc/ko_kakao/k2_a_wh.tsv", 'w', encoding='utf-8', newline='')
wr = csv.writer(f2, delimiter = '\t')

wr.writerow(["c_id", "title", "context", "q_id", "q1", "q2", "answer", "wh", "cate"])

for line in f:
    item = line.strip().split("\t")
    pa = item[2]
    id = item[0]
    title = item[1]
    q_id = item[3]
    q1 = item[4]
    q2 = item[5]
    cate = item[8]
    item[7] = item[7].replace("1", "").replace("2", "").replace("3", "")
    wh = item[7]

    if pa == "CONTENT":
        continue
    pa = pa.replace('|||||"','|||||')
    pa = pa.replace('"|||||', '|||||')
    pa = pa.replace("|||||'", "|||||")
    pa = pa.replace("'|||||", "|||||")
    data = rex_str(pa)
    # print (data)

    wr.writerow([id, title, pa, q_id, q1, q2, data, wh, cate])

    #f2.write(data)
    #f2.write("\n")