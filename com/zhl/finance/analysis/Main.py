# -*- coding: utf-8 -*-
from com.zhl.finance.analysis.dao.TextDao import text_retrive
from com.zhl.finance.analysis.perprocess.TextProcess import text_process

import jieba.analyse

if __name__ == '__main__':
    tr = text_retrive()
    docs = tr.get_by_sql("select report_content from sina_comment")

    doc_key_words=[]

    for t in docs:
        tex = t[0]
        topK = len(tex)/5
        key_words = jieba.analyse.extract_tags(tex, topK=topK,allowPOS=['ns', 'n', 'vn', 'v','nr','a','ad'])
        doc_key_words.extend(key_words)

    from collections import Counter
    # word_freq = Counter(doc_key_words)
    # wf = [(k,v) for k,v in word_freq.iteritems()]

    import matplotlib.pyplot as plt
    from os import path
    from scipy.misc import imread

    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

    wordcloud = WordCloud(font_path='./msyh.ttf', background_color='white',max_words=100, max_font_size=40, relative_scaling=.8).generate(' '.join(doc_key_words))
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    plt.show()


