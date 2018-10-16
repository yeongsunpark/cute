import concurrent.futures
import math

f1 = open("not_used.txt", "r")
lst = []
for i in f1:
    lst.append(i)
f1.close()

f2 = open("not_used_chunk_mt.txt", "w")


def write_main():
    with open("/data1/we_kor/kowiki_pages_170620_sent_chunk_10.tsv", "r") as f:
        for line in f:
            item = line.split("\t")
            title = item[1]
            for i in range(0, len(lst)):
                if title.strip() == lst[i].strip():
                    f2.write(line)
                    # f2.write("\n")


f2.close()


def main():
    workers = 30
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as exe:
        fs = {exe.submit(write_main) for n in range(0, len(qas))}

if __name__ == '__main__':
    main()