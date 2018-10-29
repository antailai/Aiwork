# coding:gbk
'''
    ����һ��·������ȡ����·���µ����ݣ�������Щ���ݼ��е�����Ƭ��
'''
import json
import os
from xpinyin import Pinyin
from pypinyin import lazy_pinyin, Style

wd = dict()  # word_list


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
    p = Pinyin()
    file = open(hanzi_path)
    for line in file.readlines():
        for each_word in line:
            next_dict = dict()
            tmp_word = {
                'word':
                each_word,
                'pinyin':
                'lue' if p.get_pinyin(each_word) == 'lve' else
                p.get_pinyin(each_word),
                'count':
                0,
                'next_dict':
                next_dict
            }
            wd[each_word] = tmp_word


if __name__ == '__main__':
    # load_hanzi_list("../lib/һ�������ֱ�.txt")
    # for key in wd:
    #     print(key, wd[key])
    # pinyin = 'lue' if (lazy_pinyin('��') == (['lve']
    #                                         or ['nve'])) else lazy_pinyin('��')
    # p = Pinyin()
    # print('lue' if p.get_pinyin('ܳ') == 'lve' else p.get_pinyin('ܳ'))
    # print(lazy_pinyin('��', style=Style.NORMAL))
