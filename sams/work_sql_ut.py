import re

def insert_str(string, s_index, e_index, str_to_insert="|||||"):
    return string[:s_index] + str_to_insert + string[s_index:e_index] + str_to_insert + string[e_index:]

def regu (c):
    p = re.compile(r"[|]{5}(.*)[|]{5}")
    m = p.search(c)
    return m.group(1)
