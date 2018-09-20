import json

f1 = open("data/duplicated_data (2).txt", "r")
f2 = open("/home/msl/data/mrc/ko_kaka/ko_mrc_v10wh_squad_pretty.json", "r")
json_data1 = json.load(f2)
f3 = open("data/check_wh.txt","a")

for line in f1:
    item = line.strip().split("\t")
    id = item[0]

    if "10_" in id:
        for doc in json_data1['data']:
            for p, t in zip(doc['paragraphs'], doc['title']):
                title = doc['title']
                wh = doc['wh']
                for qa in p['qas']:
                    q_id = qa['id']
                    if id == q_id:
                        w = "\t".join([q_id, wh])
                        f3.write(w)
                        f3.write("\n")