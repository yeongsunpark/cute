import json
import random

read_json_path1 = 'ko_wiki_v1_squad_dev.json'
write_json_path1 = 'ko_wiki_model_example.json'
read_json_path2 = '/home/msl/data/mrc/output/ko_cv/ko_cv_v1_squad_train.json'
write_json_path2 = 'ko_cv_split_v1_squad_train.json'

with open(read_json_path1, 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)
# with open(read_json_path2, 'r', encoding='utf-8') as f2:
    # json_data2 = json.load(f2)

# json_data1['data'] = random.shuffle(json_data1['data'])
# json_data2['data'] = random.shuffle(json_data2['data'])

json_data1['data'] = (json_data1['data'][:28])
# json_data2['data'] = (json_data2['data'][:207])

a = str(json_data1)
print (a.count('id'))


with open(write_json_path1, 'w', encoding='utf-8') as wf:
    json.dump(json_data1, wf, ensure_ascii=False)
# with open(write_json_path2, 'w', encoding='utf-8') as wf:
    # json.dump(json_data2, wf, ensure_ascii=False)
