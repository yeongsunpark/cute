f1 = open("not_used.txt", "r")
lst = []
for i in f1:
    lst.append(i)
f2 = open("not_used_chunk.txt", "w")

with open("/data1/we_kor/kowiki_pages_170620_sent_chunk_10.tsv", "r") as f:
    for line in f:
        item = line.split("\t")
        title = item[1]
        for i in range(0, len(lst)):
            if title.strip() == lst[i].strip():
                f2.write(line)
                # f2.write("\n")
f2.close()