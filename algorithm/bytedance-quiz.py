import re
import sys

input0 = '[I love byte apple bytedance]'
sentence = 'Ilovebytappleebytebytedance'

words = input0.strip('[]').split()

words_exists = []
long_word = ''
match = True

while len(sentence) and match:
    match = False
    for w in words:
        m = re.findall(r'' + w + r'', sentence)
        if m:
            match = True
            words_exists.append(m[0])
            if len(m[0]) > len(long_word):
                long_word = m[0]

    sentence = sentence.replace(long_word, '')
    long_word = ''

if sentence:
    words_exists.append(sentence)


print(set(words_exists).issubset(set(words)))