# -*- coding: utf-8 -*-
from com.zhl.finance.analysis.dao.TextDao import text_retrive
from com.zhl.finance.analysis.perprocess.TextProcess import text_process

import jieba.analyse

if __name__ == '__main__':
    tr = text_retrive()
    docs = tr.get_by_sql("select report_content from sina_comment")

    doc_key_words = []

    for t in docs:
        tex = t[0]
        topK = len(tex) / 5
        key_words = jieba.analyse.extract_tags(tex, topK=topK,
                                               allowPOS=['ns', 'n', 'vn', 'v', 'vd', 'nr', 'a', 'ad', 'an', 'd', 'i',
                                                         'ns', 'nt',
                                                         'nz'])
        doc_key_words.extend(key_words)

    from collections import Counter
    # word_freq = Counter(doc_key_words)
    # wf = [(k,v) for k,v in word_freq.iteritems()]

    import matplotlib.pyplot as plt
    from os import path
    from scipy.misc import imread

    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

    #
    # wordcloud = WordCloud(font_path='./msyh.ttf', background_color='white', max_words=100, max_font_size=40,
    #                       relative_scaling=.8).generate(' '.join(doc_key_words))
    # plt.figure()
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()

    d = path.dirname(__file__)

    # Read the whole text.
    # text = open(path.join(d, 'constitution.txt')).read()
    text = ' '.join(doc_key_words)
    back_coloring = imread(path.join(d, "./love.jpg"))
    # Generate a word cloud image
    # wordcloud = WordCloud(font_path='./msyh.ttf', width=800, height=600, background_color='black').generate(text)
    wordcloud = WordCloud(font_path='./msyh.ttf',  # 设置字体
                          background_color="white",  # 背景颜色
                          max_words=1000,  # 词云显示的最大词数
                          mask=back_coloring,  # 设置背景图片
                          max_font_size=200,  # 字体最大值
                          random_state=42,
                          width=600,
                          height=500,
                          )
    # Display the generated image:
    # the matplotlib way:
    wordcloud.generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
