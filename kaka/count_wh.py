result = {}

# with open ("data/check_wh.txt", "r") as f:
with open ("/home/msl/data/mrc/ko_mrc_ka/text_sum.tsv", "r") as f:
    for line in f:
        item = line.split("\t")
        # wh = item[1]
        if len(item) == 13:
            wh = item[8]
        elif len(item) == 9:
            wh = item[5]
        if wh in result:
            result[wh] +=1
        else:
            result[wh] = 1

with open ("data/count_5000.txt", "w") as f2:
    f2.write(str(result))