import csv
import json
read_json_path = '/home/msl/data/mrc/ko_law/ko_mrc_v1_squad.json'
write_txt_path = 'why.tsv'
with open(read_json_path, 'r', encoding = 'utf-8') as f1:
    json_data1 = json.load(f1)

f2 = open(write_txt_path, 'w', encoding='utf-8', newline='')
wr = csv.writer(f2, delimiter = '\t')

for doc in json_data1['data']:
    for p, t in zip (doc ['paragraphs'], doc['title']):
        for qa in p['qas']:
            # answer_end = qa['answers'][0]['answer_end']
            answer_start = qa['answers'][0]['answer_start']
print (qa['answers'])
print (qa['answers'][0])
print (qa['answers'][0]['answer_start'])
print (qa['answers'][0]['text'])
print (qa['answers'][0]['answer_end'])
aa = qa['answers'][0]['answer_end']
print(aa)
