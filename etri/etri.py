import json
read_json_path = '/home/msl/data/mrc/ko_wiki3/ko_mrc_v2_squad_pretty.json'
write_txt_path = 'etri_ys.txt'

with open(read_json_path, 'r', encoding = 'utf-8') as f1:
    json_data1 = json.load(f1)
f2 = open(write_txt_path, 'w')
for doc in json_data1['data']:
    for p, t in zip (doc ['paragraphs'], doc['title']):
        title = doc['title']
        f2.write("\n")
        f2.write("\t")
        f2.write("title")
        f2.write("\t\t\t")
        f2.write(title)
        content = p['context']
        f2.write("\n")
        f2.write("\t")
        f2.write("paragraphs")
        f2.write("\n")
        f2.write("\t\t")
        f2.write("context")
        f2.write("\t\t")
        f2.write(content)
        f2.write("\n")
        f2.write("\t\t")
        f2.write("qas")
        for qa in p['qas']:
            q_id = qa['id']
            question = qa['question']
            text = qa['answers'][0]['text']
            answer_start = qa['answers'][0]['answer_start']
            f2.write("\n")
            f2.write("\t\t\t")
            f2.write("id")
            f2.write("\n")
            f2.write("\t\t\t\t\t")
            f2.write(q_id)
