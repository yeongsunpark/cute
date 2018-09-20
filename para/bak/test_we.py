#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

exe_path = os.path.realpath(sys.argv[0])
bin_path = os.path.dirname(exe_path)
lib_path = os.path.realpath(bin_path + '/../lib/python')
sys.path.append(lib_path)

import grpc

from common.config import Config
from maum.brain.we import wordembedding_pb2
from maum.brain.we import wordembedding_pb2_grpc


class WordEmbeddingAnalysis:
    conf = Config()
    conf.init('brain-ta.conf')
    stub = None

    def __init__(self):
        remote = 'localhost:' + self.conf.get('brain-ta.nlp.word_embedding')
        channel = grpc.insecure_channel(remote)
        self.stub = wordembedding_pb2_grpc.WordEmbeddingServiceStub(channel)

    def get_word_embedding_result(self, text):
        """
        :type talk: object
        """
        input_text = wordembedding_pb2.WordEmbeddingInputText()
        input_text.text = text
        document = self.stub.GetWordEmbedding(input_text)
        word_embedding_analysis_level = wordembedding_pb2.WordEmbeddingAnalysisLevel.DESCRIPTOR
        analysis_level = ""
        word_result = []
        similarity_result = []

        if not document:
            print "document is empty"
        else:
            analysis_level = document.analysis_level
            word_result = document.word
            similarity_result = document.similarity

        result = ""
        comment = ""
        if analysis_level == word_embedding_analysis_level.values_by_name['WORD_EMBEDDING_SINGLE_WORD'].number:
            comment = "입력하신 단어는 형태소 분석을 거쳐 Word Embedding을 수행하기 때문에 다를 수 있습니다.\n"
            comment = comment + "출력은 다음과 같은 형태입니다.\n"
            comment = comment + "순위\t단어\t유사도\t\n"
            for i in range(0, len(word_result)):
                result += str(i + 1) + ".\t" + word_result[i] + "\t" + str(similarity_result[i]) + "\n"
            result = result.strip()
            comment = comment + result + "\n"
        elif analysis_level == word_embedding_analysis_level.values_by_name['WORD_EMBEDDING_TWO_WORDS'].number:
            result = "입력하신 단어는 형태소 분석을 거쳐 Word Embedding을 수행하기 때문에 다를 수 있습니다.\n"
            words = word_result[0].split(' ')
            result = result + "입력 하신 단어들은 " + words[0] + " , " + words[1] + " 입니다.\n"
            result = result + "두 단어간의 유사도는 " + str(similarity_result[0]) + " 입니다.\n"
            result = result.strip()
            comment = comment + result + "\n"
        elif analysis_level == word_embedding_analysis_level.values_by_name['WORD_EMBEDDING_MULTIPLE_WORDS'].number:
            comment = "입력하신 단어는 형태소 분석을 거쳐 Word Embedding을 수행하기 때문에 다를 수가 있습니다.\n"
            comment = comment + "출력은 다음과 같은 형태입니다.\n"
            comment = comment + "순위\t단어\t유사도\t\n"
            for i in range(0, len(word_result)):
                result += str(i + 1) + ".\t" + word_result[i] + "\t" + str(similarity_result[i]) + "\n"
            result = result.strip()
            comment = comment + result + "\n"

        elif analysis_level == word_embedding_analysis_level.values_by_name['WORD_EMBEDDING_SENTENCE_WORDS'].number:
            comment = "입력하신 문장에서 명사를 추출하여 Word Embedding을 통해 단어 간의 유사도를 구합니다.\n"
            comment = comment + "입력하신 문장에서 추출한 명사는 다음과 같습니다.\n"
            comment = comment + "출력은 다음과 같은 형태입니다.\n"
            comment = comment + "순위\t단어\t유사도\t\n"
            for i in range(0, len(word_result)):
                result += str(i + 1) + ".\t" + word_result[i] + "\t" + str(similarity_result[i]) + "\n"
                result = result.strip()
                comment = comment + result + "\n"

        return comment

if __name__ == '__main__':
    analyze = WordEmbeddingAnalysis()
    while True:
        text = raw_input('Input : ')
        if text == "quit" or text == "QUIT" or text == "q" or text == "Q":
            print("Exit the Word Embedding")
            break
        comment = analyze.get_word_embedding_result(text)
        print comment

