# coding:gbk
'''
    给定一个路径，读取所有路径下的数据，返回这些数据集中的正文片段
'''
import json
import os
from xpinyin import Pinyin

wd = dict()  # word_list


class word:
    def __init__(self, word, count, pinyin, next_data):
        self.word = word
        self.count = count
        self.pinyin = pinyin
        self.next_data = next_data


def resolve_json(path, text, title, time, url):
    f = open(path, "r")
    for line in f.readlines():
        filejson = json.loads(line)
        text.append(filejson['html'])
        title.append(filejson['title'])
        time.append(filejson['time'])
        url.append(filejson['url'])
    return (text, title, time, url)


def load_dir(path):
    text = []
    title = []
    time = []
    url = []
    if os.path.isdir(path):
        files = os.listdir(path)
        for file in files:
            if not os.path.isdir(file):
                resolve_json(path + "/" + file, text, title, time, url)
    else:
        resolve_json(path, text, title, time, url)
    return text


def load_hanzi_list(hanzi_path):
    file = open(hanzi_path)
    for line in file.readlines():
        for each_word in line:
            p = Pinyin()
            next_dict = dict()
            tmp_word = {
                'word': each_word,
                'pinyin': p.get_pinyin(each_word),
                'count': 0,
                'next_dict': next_dict
            }
            wd[each_word] = tmp_word


# if __name__ == '__main__':
#     load_hanzi_list("../lib/一二级汉字表.txt")
#     for key in wd:
#         print(key, wd[key])
