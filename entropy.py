import math
import word2phrase

def info_entropy(out_sentences,new_words): # new_word 是一个set
    word_prefix = {}
    word_suffix ={}
    word_pre_suf_entropy = {}
    for token in new_words:
        word_prefix[token] = {}
        word_suffix[token] = {}
    for line in out_sentences:
        line = ["start"] + line + ["end"]
        for i,token in enumerate(line[1:len(line)-1]):
            if token in new_words:
                if line[i] in word_prefix[token]: # 统计前缀
                    word_prefix[token][line[i]] +=1
                else:
                    word_prefix[token][line[i]] = 1
                if line[i+2] in word_suffix[token]: # 统计后缀
                    word_suffix[token][line[i+2]] +=1
                else:
                    word_suffix[token][line[i+2]] = 1
    for token in new_words:
        # calculate pre entropy
        total =0
        for k,v in word_prefix[token].items():
            total += int(v)
        pre_entropy = 0
        for k,v in word_prefix[token].items():
            pre_entropy += -(int(v)/total)*math.log(int(v)/total)
        # suf entropy
        total = 0
        for k,v in word_suffix[token].items():
            total += int(v)
        suf_entropy = 0
        for k,v in word_suffix[token].items():
            suf_entropy += -(int(v) / total) * math.log(int(v) / total)
        word_pre_suf_entropy[token] = [pre_entropy,suf_entropy]
    return word_pre_suf_entropy
import read_data
book_sentences = read_data.get_sentences('c://users//stifler//desktop//data.txt')
out_sentences,new_words = word2phrase.train_model(book_sentences,threshold=100)
for i in new_words:
    print(i)
word_pre_suf_entropy = info_entropy(out_sentences,new_words)
for i in word_pre_suf_entropy:
    print(i)
