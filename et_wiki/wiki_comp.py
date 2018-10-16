f2 = open("new_chunk.txt", "w")

with open("/data1/we_kor/kowiki_pages_170620_sent_chunk_10.tsv", "r") as f:
    for line in f:
        item = line.split("\t")
        title = item[1]
        f2.write(title)
        f2.write("\n")
f2.close()