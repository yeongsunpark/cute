f1 = open("short_list.txt", "r")
lst = []
for i in f1:
    lst.append(i)

print (lst[0].split("\t")[6])


f2 = open("compare.txt", "w")

with open ("origin_신2_result.txt", "r") as f:
    for line in f:
        item = line.split("\t")
        if len(item) == 2:
            answer = item[1]
            for i in range(0, len(lst)):
                if answer.strip() == lst[i].split("\t")[6].strip():
                    print(answer)
                    f2.write(item[0])
                    f2.write("\t")
                    f2.write(item[1])
                    f2.write("\n")

f2.close()