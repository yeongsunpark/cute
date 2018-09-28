import json

read_json_path1 = '/home/msl/data/mrc/output/ko_cv/ko_cv_v42_squad_dev.json'
read_json_path2 = '/home/msl/data/mrc/output/ko_cv/ko_cv_vhana_squad_dev.json' 
#read_json_path2 = '/home/msl/data/mrc/output/ko_revision/ko_revision_v2_squad_train.json'
write_json_path = 'ko_extend_hana42_squad_dev.json'

with open(read_json_path1, 'r', encoding='utf-8') as f1:
    json_data1 = json.load(f1)
with open(read_json_path2, 'r', encoding='utf-8') as f2:
    json_data2 = json.load(f2)

json_data1['data'].extend(json_data2['data'])

with open(write_json_path, 'w', encoding='utf-8') as wf:
    json.dump(json_data1, wf, ensure_ascii=False)

