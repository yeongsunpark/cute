import csv
import json

read_json_path = '/home/msl/data/mrc/ko_law/ko_mrc_v1_squad.json'
write_txt_path = 'etri_law_1.tsv'

with open(read_json_path, 'r', encoding = 'utf-8') as f1:
    json_data1 = json.load(f1)

f2 = open(write_txt_path, 'w', encoding='utf-8', newline='')
wr = csv.writer(f2, delimiter = '\t')

wr.writerow(["version", "", "", "", "", "1"])
wr.writerow(["creator", "", "", "", "", "mindslab"])
wr.writerow(["data"])

for doc in json_data1['data']:
    for p, t in zip (doc ['paragraphs'], doc['title']):
        title = doc['title']
        wr.writerow(["", "title", "", "", "", title])

        content = p['context']
        wr.writerow(["","paragraphs"])
        wr.writerow(["", "", "context", "", "", content])
        wr.writerow(["", "", "context_en"])
        wr.writerow(["", "", "context_tagged"])
        wr.writerow(["", "", "qas"])

        for qa in p['qas']:
            # if '-1' not in str(qa['id']):
                q_id = qa['id']
                question = qa['question']
                wr.writerow(["", "", "", "id", "", q_id])
                wr.writerow(["", "", "", "question", "", question])
                wr.writerow(["", "", "", "question_en"])
                wr.writerow(["", "", "", "question_tagged"])
                wr.writerow(["", "", "", "questionType"])
                wr.writerow(["", "", "", "questionFocus"])
                wr.writerow(["", "", "", "questionSAT"])
                wr.writerow(["", "", "", "questionLAT"])

                text = qa['answers'][0]['text']
                answer_start = qa['answers'][0]['answer_start']
                answer_end = qa['answers'][0]['answer_end']
                # answer_end = 0
                wr.writerow(["", "", "", "answers"])
                wr.writerow(["", "", "", "", "text", text])
                wr.writerow(["", "", "", "", "text_en"])
                wr.writerow(["", "", "", "", "text_tagged"])
                wr.writerow(["", "", "", "", "text_syn"])
                wr.writerow(["", "", "", "", "answer_start", answer_start])
                wr.writerow(["", "", "", "", "answer_end", answer_end])

f2.close()