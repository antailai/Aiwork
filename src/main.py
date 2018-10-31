# coding:gbk

import train
import load
import re


def init_emission():
    # qing->�壺10 �룺2 (for example) qing -> �壺10/12 �룺2/12
    # wd[��] = {'word'= �� 'pinyin' = qing 'count' = 0 'next_dict' = {'��' = 10 '��' =5}}
    # py [qing] = (��������������������������������������������������)
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
    # wd[��] = {'word'= �� 'pinyin' = qing 'count' = 0 'next_dict' = {'��' = 10 '��' =5}} (for example) next_dict = {'��' = 10/15 '��' = 5/15}
    for key in load.wd:
        sum = 0
        for word in load.wd[key]['next_dict']:
            sum += load.wd[key]['next_dict'][word]
        for word in load.wd[key]['next_dict']:
            load.wd[key]['next_dict'][word] /= sum


def transfer(input_path):
    input = open(input_path)  # open the input.txt
    tmp_sentence = []
    for line in input.readlines():
        line = re.sub('\n', '', line)
        tmp = line.split(" ")  # ��ÿ��ƴ���ֿ�д��list
        for item in tmp:  # ����ÿ��ƴ��
            tmp_list = list()
            for key in load.py[item]:
                tmp_list.append(key)
            tmp_sentence.append(tmp_list)
    return tmp_sentence


if __name__ == '__main__':
    load.load_hanzi_list("D://project//Aiwork/lib/һ�������ֱ�.txt")
    train.train("D://project/Aiwork/data_set/2016-10.txt")
    load.load_pyhz_list("D://project/Aiwork/lib/ƴ�����ֱ�.txt")
    init_emission()
    init_tramsition()

    # for key in transfer.py:
    #     for word in transfer.py[key]:
    #         print(word, transfer.py[key][word])