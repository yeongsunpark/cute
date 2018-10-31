import csv
import json

read_json_path = '/home/msl/data/mrc/output/ko_law/ko_law_v1_squad_dev.json'
write_txt_path = 'ys_ko_law_v1_squad_dev.tsv'

with open(read_json_path, 'r', encoding = 'utf-8') as f1:
    json_data1 = json.load(f1)

f2 = open(write_txt_path, 'w', encoding='utf-8', newline='')
wr = csv.writer(f2, delimiter = '\t', quoting=csv.QUOTE_NONE, quotechar='')

for doc in json_data1['data']:
    for p, t in zip (doc ['paragraphs'], doc['title']):
        title = doc['title']
        content = p['context_original']

        for qa in p['qas']:
            if '-1' in str(qa['id']):
                q_id = qa['id']
                question = qa['question_original']
                text = qa['answers'][0]['text_original']
                answer_start = qa['answers'][0]['answer_start']
                answer_end = qa['answers'][0]['answer_end']
            else:
                q_id2 = qa['id']
                question2 = qa['question_original']
        wr.writerow([title, content, q_id, question, q_id2, question2, text, answer_start, answer_end])

f2.close()
