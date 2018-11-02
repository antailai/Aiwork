# coding:gbk

import json
import os
import re
# from xpinyin import Pinyin
from pypinyin import lazy_pinyin, load_single_dict

wd = dict()  # word_list
py = dict()

load_single_dict({ord('帧'): 'zhen'})
load_single_dict({ord('嗯'): 'en'})
load_single_dict({ord('嗲'): 'dia'})
load_single_dict({ord('芎'): 'xiong'})
load_single_dict({ord('菹'): 'zu'})
load_single_dict({ord('呒'): 'fu'})
load_single_dict({ord('丬'): 'pan'})
load_single_dict({ord('嬷'): 'mo'})
load_single_dict({ord('珩'): 'heng'})
load_single_dict({ord('砉'): 'hua'})
load_single_dict({ord('碡'): 'zhou'})
load_single_dict({ord('聒'): 'guo'})
load_single_dict({ord('蚵'): 'ke'})
load_single_dict({ord('豉'): 'chi'})
load_single_dict({ord('霰'): 'xian'})


def load_pyhz_list(pinyin2hanzi_path):
    pinyin2hanzi = open(pinyin2hanzi_path)
    hanzi = open("D://project/Aiwork/lib/一二级汉字表.txt").read()
    for line in pinyin2hanzi.readlines():
        line = re.sub('\n', '', line)
        tmp = line.split(" ")
        tmp_pinyin = tmp[0]
        tmp_dict = dict()
        for i in range(1, len(tmp)):
            if tmp[i] in hanzi:
                tmp_dict.setdefault(tmp[i], {'start': 0, 'count': 0})
        py.setdefault(tmp_pinyin, tmp_dict)
    return py


'''
    给定一个路径，读取所有路径下的数据，返回这些数据集中的正文片段
'''


def load_dataset(path, text, title, time, url):
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
                load_dataset(path + "/" + file, text, title, time, url)
    else:
        load_dataset(path, text, title, time, url)
    return text


def load_hanzi_list(hanzi_path):
    file = open(hanzi_path)
    for line in file.readlines():
        for each_word in line:
            resolve_pinyin = []
            if lazy_pinyin(each_word) == ['lve']:
                resolve_pinyin = 'lue'
            elif lazy_pinyin(each_word) == ['nve']:
                resolve_pinyin = 'nue'
            else:
                resolve_pinyin = ''.join(lazy_pinyin(each_word))
            tmp_word = {
                'word': each_word,
                'pinyin': resolve_pinyin,
                'count': 0,
                'start_count': 0,
                'next_dict': {}
            }
            wd[each_word] = tmp_word
