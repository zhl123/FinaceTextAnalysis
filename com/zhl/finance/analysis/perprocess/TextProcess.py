# -*- coding: utf-8 -*-
import jieba.analyse

class text_process(object):

    def __init__(self):
        pass

    def extract_key_words(self, text, topK=20):
        jieba.analyse.extract_tags(text, topK=topK, allowPOS=['ns', 'n', 'vn', 'v','nr','a','ad'])