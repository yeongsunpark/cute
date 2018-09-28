# -*- coding:utf-8 -*-

import re

m = re.sub(r'([.])(\d)',
          r'\1 \2',
'''I am a princess.1 she is. number2다. 3이렇게 숫자가 떼져있음 띄지마세요
요거는.1번 떼보세요
''')
# print (m)

# 반복되는 문자 지우기
n = re.sub(r'(.+)\1',
           r'\1',
           """반반복복되되는 문자를 지지워워주세요요.
pleaase remmovee""")
# print (n)

# 반복되는 단어 지우기
n = re.sub(r'(.+) \1',
           r'\1',
           """반복 반복 반복 되는 되는 문자를 지워 지워 주세요.
           """)
# print (n)

# 반복되는 단어 지우기 (2)
n = re.sub(r'(.+) \1 \1',
           r'\1',
           """반복 반복 반복 되는 되는 문자를 지워 지워 주세요.
           """)
# print (n)

# 반복되는 단어 지우기 (2)
"""
f = open('redun.txt', 'r')
f2 = open('redunout.txt', 'w')
data = f.read()

def duplicate_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
n = data
a = ' '.join(duplicate_list(n.split()))
f2.write(a)
f2.write("\n")
f.close()
f2.close()
"""


f = open('redun.txt','r')
f2 = open('redunout.txt', 'w')
data = f.read()

n = re.compile(r'(.+) \1')
m = re.compile(r'(.+) \1 \1')

f2.write(m)
f.close()
f2.close()