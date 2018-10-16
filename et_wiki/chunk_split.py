f = open("not_used_chunk_moon.txt","r")
data = f.readlines()
data7 = data[700000:]
f2 = open("result_70000.txt","w")
for d in data7:
    if len(d) >= 200:
        f2.write(d)
# f2.write("".join(data[700000:]))
f.close()
f2.close()
