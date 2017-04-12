from string import punctuation


def remove_punctuation(s):
    p = punctuation
    text = filter(lambda x : x not in p, s)
    text = map(lambda x : x.strip(), text.split())
    d = {}
    for i in text:
        if i not in d:
            d[i] = 0
        d[i]+=1
    return d

s = '   I &*()(@@#$%)   am    !!!!'

remove_punctuation(s)