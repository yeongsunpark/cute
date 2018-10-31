def extract_str(string, s_index, e_index):
    # return string[:index] + str_to_insert + string[index:]
    return string[s_index:e_index]


f = open("/home/msl/ys/cute/sams/select.txt", "r")
f2 = open("/home/msl/ys/cute/sams/select_result.txt", "w")

for line in f:
    item = line.split("\t")
    data = extract_str(item[2], int(item[6]), int(item[7]))
    f2.write("\t".join([data, item[5]]))
    f2.write("\n")