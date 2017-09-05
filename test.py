from itertools import tee,zip_longest
from textblob import TextBlob
import nltk
import re
import math

def pairwise(iterable):
    """
    Adjacent pairs with overlap
    >>> list(pairwise(range(5)))
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, None)]
    """
    a, b = tee(iterable) # tee returns n independent iterable objects
    next(b)
    # return an iterator that aggregate elements from each of the iterators
    # zip_longest((a,b,c),(1,2)) => ((a,1),(b,2),(c,_))
    return zip_longest(a, b)

def info_entropy(data,new_words): # new_word 是一个set
    word_prefix = {}
    word_suffix ={}
    word_pre_suf_entropy = {}
    for token in new_words:
        word_prefix[token] = {}
        word_suffix[token] = {}
    for line in data:
        line = ["start"] + line + ["end"]
        for i,token in enumerate(line[1:len(line)-1]):
            if token in new_words:
                if line[i] in word_prefix[token]: # 统计前缀
                    word_prefix[token][line[i]] +=1
                else:
                    word_prefix[token][line[i]] == 1
                if line[i+2] in word_suffix[token]: # 统计后缀
                    word_suffix[token][line[i+2]] +=1
                else:
                    word_suffix[token][line[i+2]] == 1
    for token in new_words:
        # calculate pre entropy
        total =0
        for k,v in word_prefix[token]:
            total += v
        pre_entropy = 0
        for k,v in word_prefix[token]:
            pre_entropy += -(v/total)*math.log(v/total)
        # suf entropy
        total = 0
        for k, v in word_suffix[token]:
            total += v
        suf_entropy = 0
        for k, v in word_suffix[token]:
            suf_entropy += -(v / total) * math.log(v / total)
        word_pre_suf_entropy[token] = [pre_entropy,suf_entropy]
    return word_pre_suf_entropy

line = [0]+[1,2,3,4]+[5]
print(line)