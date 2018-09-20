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

        if analysis_level == word_embedding_analysis_level.values_by_name['WORD_EMBEDDING_SINGLE_WORD'].number:
            result = list()
            for i in range(0, len(word_result)):
                if similarity_result[i] >= 0.85:
                    #print word_result[i], word_result[i].find('ㄴ')
                    if not word_result[i].find('ㄴ') > -1:
                        result.append(word_result[i])
        return result

if __name__ == '__main__':
    analyze = WordEmbeddingAnalysis()
    while True:
        text = raw_input('Input : ')
        if text == "quit" or text == "QUIT" or text == "q" or text == "Q":
            print("Exit the Word Embedding")
            break
        result = analyze.get_word_embedding_result(text)
        for resul in result: 
            print resul

