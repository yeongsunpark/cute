def insert_str(string, str_to_insert, s_index, e_index):
    # return string[:index] + str_to_insert + string[index:]
    return string[:s_index] + str_to_insert + string[s_index:e_index] +  str_to_insert + string[e_index:]

f = open ("data/wa.txt", "r")
f2 = open ("data/wa_res.txt", "w")

for line in f:
    item = line.strip().split("\t")
    s_index = int(item[0].replace(u"\ufeff", ''))
    answer = item[6]
    context = item[7]
    e_index = s_index + len(answer)
    str_to_insert = "|||||"

    data = insert_str(context, str_to_insert, s_index, e_index)

    f2.write(data)
    f2.write("\n")