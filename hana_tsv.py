import json

read_json_path = '/home/msl/data/mrc/ko_law/ko_mrc_v1_squad.json'
write_txt_path = '/home/msl/data/mrc/ko_law/ko_mrc_v1_squad_next.tsv'

with open(read_json_path, 'r', encoding = 'utf-8') as f1:
    json_data1 = json.load(f1)

f2 = open(write_txt_path, 'w', encoding='utf-8', newline='')
tmp = []
for doc in json_data1['data']:
    for p in doc['paragraphs']:
        context = p['context']
        if context !=tmp:
            f2.write("\n")
            f2.write(context)
        temp = context
        for qa in p ['qas']:
            q_id = qa['id']
            q_ori = qa ['question']
            f2.write("\t")
            f2.write(q_ori)
f2.close()
