# coding:gbk
'''
    给定一个路径，读取所有路径下的数据，返回这些数据集中的正文片段
'''
import json
import os
from xpinyin import Pinyin

wd = []  # word_list


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
            tmp_word = each_word
            tmp_pinyin = p.get_pinyin(tmp_word)
            tmp_next_data = dict()
            tmp_count = 0
            word1 = word(tmp_word, tmp_count, tmp_pinyin, tmp_next_data)
            wd.append(word1)


# if __name__ == '__main__':
#     load_hanzi_list(
#         "D:\cloud\Seafile\project\python\AIwork-pinyin\lib\一二级汉字表.txt")
#     for item in wd:
#         print(item.word, end=' ')
#         print(item.count, end=' ')
#         print(item.pinyin, end=' ')
#         print(item.next_data)
