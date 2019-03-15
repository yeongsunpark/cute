#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by YeongsunPark at 2019-02-27
import re

"""
import sys, os
import json
import time
import re

context = "나는 파리의 택시 운전사"
answer = "택시"

start = (context.find(answer))
end = (context.find(answer)+len(answer))

print (start, end)

m_context = context[:start] + "|"*5 + answer + "|"*5 + context[end:]
print (m_context)
"""

# result = []
# re_splitter = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s")
# re_splitter = re.compile(r"(?<=\.|\?|\!)\s")  # (긍정형 후방탐색).으로 끝나거나 ?로 끝나거나 !로 끝나는 것의 뒤를 찾아.
# para ="""첨부를 확인하시고 검토의견에 대한 판단을 부탁드리며, 확인코드에 해당하는 항목에 대해서는 내부적으로 확인하시어 답변 또는 증명에 대한 준비를 부탁 드립니다. 또한 사업의 현재 진도에 대해서도 간단하게 회신을 부탁 드립니다. 기타 궁금하시거나 필요한 부분에 대해서는 언제든지 말씀해 주시기 바랍니다."""
# sentences = re_splitter.split(para)
# (sentences)

data = "안녕하세요 저는"
print (len(data))