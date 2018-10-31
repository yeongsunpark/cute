f1 = open("not_used.txt", "r")
lst = set()
for i in f1:
    lst.add(i.strip())
print (len(lst))
f1.close()
f2 = open("not_used_chunk_moon.txt", "w")

with open("/data1/we_kor/kowiki_pages_170620_sent_chunk_10.tsv", "r") as f:
    for line in f:
        item = line.split("\t")
        title = item[1].strip()
        if title in lst:
            f2.write(line)
            f2.flush()
f2.close()
