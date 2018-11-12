import json
import os

write_json_path = 'ko_mrc_cw_v1_squad_pretty.json'

filenames = os.listdir("/home/msl/data/mrc/ko_cw")
for filename in filenames:
    full_filename = os.path.join("/home/msl/data/mrc/ko_cw", filename)
    print (full_filename)
    count = 0
    if count == 0:
        with open(full_filename, "r", encoding="utf-8") as f1:
            json_data1 = json.load(f1)
        count += 1
    else:
        with open(full_filename, "r", encoding="utf-8") as f2:
            json_data2 = json.load(f2)
        json_data1['data'].extend(json_data2['data'])

    with open(write_json_path,"w", encoding='utf-8') as wf:
        json.dump(json_data1, wf, ensure_ascii=False, indent=2)
