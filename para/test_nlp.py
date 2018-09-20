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
        print json_ret

    def get_named_entity(self):
        ret = self.stub.GetNamedEntityTagList(empty_pb2.Empty())
        json_ret = json_format.MessageToJson(ret, True)
        print json_ret

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
        print doc

        # JSON text로 만들어낸다.
        json_text = json_format.MessageToJson(ret, True, True)
        print json_text
        for i in range(len(ret.sentences)):
            text = ret.sentences[i].text
            analysis = ret.sentences[i].morps
            morp = ""
            for j in range(len(analysis)):
                morp = morp + " " + analysis[j].lemma + "/" + analysis[j].type
            morp = morp.encode('utf-8').strip()
            addstr = 'morp -> ' + morp
            print addstr
            ner = ret.sentences[i].nes
            for j in range(len(ner)):
                ne = ner[j].text + "/" + ner[j].type
                ne = ne.encode('utf-8').strip()
                addNE = 'NE -> ' + ne
                print addNE

        # self.stub.AnalyzeMultiple()
        # SEE grpc.io python examples

    def is_number(self, select):
        try:
            int(select)
            return True, int(select)
        except ValueError:
            return False, select

    def test_nlp(self):
        nlp_client = NlpClient()
        #nlp_client.get_provider()
        # This is related to nlp1 and brain-ta issue 185
        #nlp_client.get_named_entity()
    
        # NLP analysis level 지정 방법
        # 1. parameter로 지정( or 변수로 할당)
        # level = 0
        # nlp_client.analyze('안녕하세요. 자연어 처리 엔진을 원격으로 호출해요.', level)

        # 2. 사용자가 입력
        while True:
            print("Usage : NLP Analysis Engine")
            print("Level 0 : All NLP Analysis With Morpheme, Named Entity, Word Sense Disambiguation, Dependency Parser, Semantic Role Labeling and Zero Anaphora")
            print("Level 1 : Word, Morpheme")
            print("Level 2 : Level 1 + Named Entity")
            print("Level 3 : Level 2 + Word Sense Disambiguation")
            print("Level 4 : Level 3 + Dependency Parser")
            print("Level 5 : Level 4 + Semantic Role Labeling")
            print("Level 6 : Level 5 + Zero Anaphora")
            print("quit : Exit the System!!")

            select = raw_input("Select NLP Analysis Level : ")

            if select == "quit":
                break

            flag, level = self.is_number(select)

            if flag == True:
                if level > 6 or level < 0:
                    print("Select Error!!")
                    print("You must type only Number range 0-2")
                    continue
                else:
                    print("Usage : Extraction Keyword Frequency Engine")
                    print("Level 0 : Extract keyword frequency with NP, VP, NamedEntity")
                    print("Level 1 : Don't extract keyword frequency with NP, VP, NamedEntity")
                    keyword_select = raw_input("Select Keyword Frequency Level :")
                    keyword_flag, keyword_level = self.is_number(keyword_select)
                    if keyword_flag == True:
                        if keyword_level > 1 or keyword_level < 0:
                            print("Select Error!!")
                            print("You must type only Number range 0-1")
                            continue
                        elif keyword_level == 0 or keyword_level ==1:
                            remote = 'localhost:' + conf.get('brain-ta.nlp.3.kor.port')
                            channel = grpc.insecure_channel(remote)
                            self.stub = nlp_pb2_grpc.NaturalLanguageProcessingServiceStub(channel)
                            start_time = time.time()
                            self.analyze("안녕하세요. 판교에 위치한 회사입니다.", level, keyword_level)
                            print(time.time() - start_time)
                        else:
                            print("Select Error!!")
                            print("You must type only Number!!")
                            continue
            else:
                print("Select Error!!")
                print("You must type only Number!!")
                continue

if __name__ == '__main__':
    conf = Config()
    conf.init('brain-ta.conf')
    nlp_client = NlpClient()
    nlp_client.test_nlp()
