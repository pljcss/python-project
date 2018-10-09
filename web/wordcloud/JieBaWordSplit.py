# -*- coding:utf-8 -*-
import jieba

comment_text = open('/Users/saicao/Desktop/file1.txt','r').read()

cut_text = " ".join(jieba.cut(comment_text))

print cut_text