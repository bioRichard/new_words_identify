import re

# 返回句子数组，list[sentence], 每个sentence也是token数组
def get_sentences(file):
    text = open(file,'r',encoding='utf-8').read()
    sentences = []
    for line in re.split('\n',text):
        for sentence in re.split('，|。|！|：|？',line):
            pa = re.compile('\(|\)')
            sentence=pa.sub('',sentence)
            if sentence != "":
                sentences.append([token for token in sentence])
    return sentences

rs = get_sentences('c://users//stifler//desktop//data.txt')
for i in rs:
    print(i)