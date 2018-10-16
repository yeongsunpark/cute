f1 = open("not_used.txt", "r")
lst = []
for i in f1:
   lst.append(i.strip())
f2 = open("not_used_chunk_wm.txt", "w")

with open("/data1/we_kor/kowiki_pages_170620_sent_chunk_10.tsv", "r") as f:
   for line in f:
       item = line.split("\t")
       title = item[1]
       if title.split() in lst:
           f2.write(line)
f2.close()