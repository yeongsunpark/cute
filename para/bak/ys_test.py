#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time

import grpc
from google.protobuf import empty_pb2
from google.protobuf import json_format

exe_path = os.path.realpath(sys.argv[0])
bin_path = os.path.dirname(exe_path)
lib_path = os.path.realpath(bin_path + '/../lib/python')
sys.path.append(lib_path)

from maum.brain.nlp import nlp_pb2
from maum.brain.nlp import nlp_pb2_grpc
from maum.common import lang_pb2
from common.config import Config


class NlpClient:
    conf = Config()
    stub = None

    def get_provider(self):
        ret = self.stub.GetProvider(empty_pb2.Empty())
        json_ret = json_format.MessageToJson(ret, True)
        #print json_ret

    def get_named_entity(self):
        ret = self.stub.GetNamedEntityTagList(empty_pb2.Empty())
        json_ret = json_format.MessageToJson(ret, True)
        #print json_ret

    def analyze(self, text, level, keyword_level):
        in_text = nlp_pb2.InputText()
        in_text.text = text
        in_text.lang = lang_pb2.kor
        in_text.split_sentence = True
        in_text.use_tokenizer = False
        in_text.level = level
        in_text.keyword_frequency_level = keyword_level

        ret = self.stub.Analyze(in_text)

        # JSON Object 로 만들어 낸다.
        printer = json_format._Printer(True, True)
        doc = printer._MessageToJsonObject(ret)
        #print doc

        # JSON text로 만들어낸다.
        json_text = json_format.MessageToDict(ret, True, True)
        return json_text
        # self.stub.AnalyzeMultiple()
        # SEE grpc.io python examples

    def morp_analyze(self, text):
        self.conf.init('brain-ta.conf')
        #nlp_client = NlpClient()

        remote = 'localhost:' + self.conf.get('brain-ta.nlp.1.kor.port')
        channel = grpc.insecure_channel(remote)
        self.stub = nlp_pb2_grpc.NaturalLanguageProcessingServiceStub(channel)

        nlp_result = self.analyze(text, 1, 1)
        # print nlp_result['sentences'][0]['morps']

        return nlp_result['sentences'][0]['morps']
        

    def ys(self, text):
        print text 
        


if __name__ == '__main__':
    nlp_client = NlpClient()
    nlp_client.morp_analyze("이 문장을 형태소 분석해봐")
    a = nlp_client.morp_analyze("서울대공원전략기획실(02-550-3332)") 
    for i in range (len(a)):
        print a[i]['lemma'], a[i]['type']
