f = open("etri_wiki_20_v2_ys.tsv", "r")
f2 = open("etri_wrong.txt", "w")

context = ""
idd = int()
text = ""
answer_start = int()
answer_end = int()
lst = []

for line in f:
    item = line.strip().split("\t")
    if item[0] == "context":
        context = item[3]
    elif item[0] == "id":
        idd = item[2]
    elif item[0] == "text":
        text = item[1]
    elif item[0] == "answer_start":
        answer_start = item[1]
    elif item[0] == "answer_end":
        answer_end = item[1]
        if "-2" in idd:
            extract = context[int(answer_start):int(answer_end)]
            datas = context, idd, text, extract, answer_start, answer_end
            f2.write("\t".join(datas))
            f2.write("\n")
    else:
        pass
# print (lst)
f.close()
f2.close()

"""
    if extract != text:
        with open("id_extract.txt", "w") as f2:
            print (extract)
            print (text)
            f2.write(idd)
"""