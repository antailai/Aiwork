# coding:gbk

import train
import load
import re


def init_emission():
    # qing->清：10 请：2 (for example) qing -> 清：10/12 请：2/12
    # wd[清] = {'word'= 清 'pinyin' = qing 'count' = 0 'next_dict' = {'华' = 10 '白' =5}}
    # py [qing] = {'清' = 10 '青' =5}
    for key in load.wd:
        load.py[load.wd[key]['pinyin']][key] = load.wd[key]['count']
    for key in load.py:
        sum = 0
        for word in load.py[key]:
            sum += load.py[key][word]
        if sum == 0:
            continue
        for word in load.py[key]:
            load.py[key][word] /= sum


def init_tramsition():
    # wd[清] = {'word'= 清 'pinyin' = qing 'count' = 0 'next_dict' = {'华' = 10 '白' =5}} (for example) next_dict = {'华' = 10/15 '白' = 5/15}
    for key in load.wd:
        sum = 0
        for word in load.wd[key]['next_dict']:
            sum += load.wd[key]['next_dict'][word]
        for word in load.wd[key]['next_dict']:
            load.wd[key]['next_dict'][word] /= sum


def transfer(input_path):
    # py [qing] = {'清' = 10 '青' =5}
    input = open(input_path)  # open the input.txt
    tmp_sentence = []
    for line in input.readlines():
        tmp_list = []
        line = re.sub('\n', '', line)
        tmp = line.split(" ")  # 将每个拼音分开写进list
        for item in tmp:  # 处理每个拼音
            tmp_word = max(load.py[item], key=load.py[item].get)
            tmp_list.append(tmp_word)
        tmp_sentence.append(tmp_list)
    return tmp_sentence


if __name__ == '__main__':
    load.load_hanzi_list("D://project//Aiwork/lib/一二级汉字表.txt")
    train.train("D://project/Aiwork/data_set")
    load.load_pyhz_list("D://project/Aiwork/lib/拼音汉字表.txt")
    init_emission()
    init_tramsition()
    tmp_sentence = transfer("D://project/Aiwork/data/input.txt")
    for sentence in tmp_sentence:
        print(sentence)
    # for key in transfer.py:
    #     for word in transfer.py[key]:
    #         print(word, transfer.py[key][word])