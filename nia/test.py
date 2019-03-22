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

data = """'마더' 고보결과 전혜진 허율의 존재를 알았다. 15일 방송된 tvN 수목드라마 '마더' 8회에서는 현진(고보결 분 )은 실종된 혜나(허율 분)의 존재를 알게 되는 모습이 전파를 탔다.이날 현진은 ""이 아이는 사망했다고 보시나요?""라고 물었다. 형사는 ""누군가가 데리고 갔을 가능성도 있다""고 대답했다. 이어 현진은 자영(고성희)의 학대정황에 대해 물었다. 아이가 학대를 당했을 정황에 대해 묻자 형사는 답할 수 없다고 했다. 현진은 계속해서 “용의자가 있나요?”라고 물었지만 창근은 “수사중이라 말 못해요”라고 밝혔다.한편 수진(이보영 분)은 이날 현진에 이어 이진 (전혜진 분)에게까지 |||||혜나|||||의 정체를 들켰다.‘마더’는 상처받은 소녀를 구해내기 위해 그 소녀의 엄마가 되기로 한 여자의 이야기를 담아냈다. 온라인 이슈팀 mkculture@mkculture.com< Copyright ⓒ MBN(www.mbn.co.kr) 무단전재 및 재배포 금지 >

"""
print (data[330:332])