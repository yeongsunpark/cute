import json

result = {}

for i in range (1, 11):
    with open("/home/msl/data/mrc/ko_kaka/ko_mrc_v{}wh_squad_pretty.json".format(i), "r") as f:
        json_data = json.load(f)

        for doc in json_data['data']:
            for p, t in zip(doc['paragraphs'], doc['title']):
                wh = doc['wh']
                if wh in result:
                    result[wh] += 1
                else:
                    result[wh] = 1

with open("data/count_wh_file.txt", "w") as f2:
    f2.write(str(result))