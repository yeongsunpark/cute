import json
import random
"""
read_json_path1 = '/home/msl/data/mrc/output/ko_revision_only/ko_revision_only_v2_squad_dev.json'

with open(read_json_path1, 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)
f2 = open("ko_id.txt", "w")

for doc in json_data1['data']:
    for p in doc['paragraphs']:
        context = p['context_original']
        for qa in p['qas']:
            q_id = qa['id']
            q_ori = qa['question_original']
            for a in qa['answers']:
                a_ori = a['text_original']
                # print('{}\t{}\t{}\t{}'.format(q_id, context, q_ori, a_ori))
                item = q_id, context, q_ori, a_ori
                f2.write("\t".join(item))
                f2.write("\n")
"""
####################
read_json_path1 = '/home/msl/ys/git/linguistic-lab/mrc_utils/extend/ko_wiki_model_example.json'
write_txt_path1 = 'demo_wiki_sample.txt'
####################
with open(read_json_path1, 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)
f2 = open(write_txt_path1, 'w')

for doc in json_data1['data']:
    for p in doc['paragraphs']:
        context = p['context_original']
        for qa in p['qas']:
            q_id = qa['id']
            q_ori = qa['question_original']
            for a in qa['answers']:
                a_ori = a['text_original']
                # print('{}\t{}\t{}\t{}'.format(q_id, context, q_ori, a_ori))
                item = q_id, context, q_ori, a_ori
                f2.write("\t".join(item))
                f2.write("\n")
f2.close()
