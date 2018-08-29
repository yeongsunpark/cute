import csv
import json




for i in range(1, 11):
    read_json_path = '/home/msl/data/mrc/ko_kaka/ko_mrc_v{}_squad_pretty.json'.format(i)
    with open(read_json_path, 'r', encoding = 'utf-8') as f1:
        json_data1 = json.load(f1)
    print (i)

    write_txt_path = 'kaka3.tsv'
    f2 = open(write_txt_path, 'a', encoding='utf-8', newline='')
    for doc in json_data1['data']:
        for p, t in zip(doc['paragraphs'], doc['title']):
            title = doc['title']
            cate = doc['cate']
            for qa in p['qas']:
                if '-1' in str(qa['id']):
                    q_id = qa['id']
                    question = qa['question']
                    f2.write(question)
                    f2.write("\n")
                    text = qa['answers'][0]['text']
                    answer_start = qa['answers'][0]['answer_start']
                    answer_end = qa['answers'][0]['answer_end']
                    # print (answer_start)