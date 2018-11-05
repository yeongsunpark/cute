f1 = open("old_emails.txt", "r")
# 박영선  a
# 이원문  b
# 카카오  c
# 박영선  d
# 이원문  e

lst = list()
for ff in f1:
    ff = ff.replace("\n", "")
    i = ff.split("\t")
    lst.append(i)
f1.close()
print(lst)


f2 = open("not_dup_emails.txt", "w")


with open("new_emails.txt", "r") as f:
    # 박영선  parkys  a
    # 이원문  moon    b
    # 카카오  kakao   c
    # 박영선  ylunar  x
    # 이원문  moon    y

    for line in f:
        item = line.split("\t")
        name = item[0].strip()
        id = item[2].strip()
        flag = True

        for l in lst:
            if name == l[0] and id == l[1]:
                flag = False
                break
        if flag:
            f2.write(line)


f2.close()