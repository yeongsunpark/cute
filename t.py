answer = "안녕"
marker = "|"
context = "여러분|||||안녕|||||하세요"

if "{}{}{}".format(marker*5, answer, marker*5) in context:
    print ("-")

import re
p = re.compile(r"[|]{5}(.*)[|]{5}")
def regu (c):
    m = p.search(c)
    return m.group(1)

if __name__ == "__main__":
    context = "여러분|||||안녕|||||하세요"
    a = regu(context)