# coding:gbk

import train
import transfer
import load


def init_emission():
    # qing->�壺10 �룺2 (for example) qing -> �壺10/12 �룺2/12
    # wd[��] = {'word'= �� 'pinyin' = qing 'count' = 0 'next_dict' = {'��' = 10 '��' =5}}
    # py [qing] = (��������������������������������������������������)
    for key in load.wd:
        transfer.py[load.wd[key]['pinyin']][key] = load.wd[key]['count']
    for key in transfer.py:
        sum = 0
        for word in transfer.py[key]:
            sum += transfer.py[key][word]
        for word in transfer.py[key]:
            transfer.py[key][word] /= sum


def init_tramsition():
    # wd[��] = {'word'= �� 'pinyin' = qing 'count' = 0 'next_dict' = {'��' = 10 '��' =5}} (for example) next_dict = {'��' = 10/15 '��' = 5/15}
    for key in load.wd:
        sum = 0
        for word in load.wd[key]['next_dict']:
            sum += load.wd[key]['next_dict'][word]
        for word in load.wd[key]['next_dict']:
            load.wd[key]['next_dict'][word] /= sum


if __name__ == '__main__':
    load.load_hanzi_list("D://project//Aiwork/lib/һ�������ֱ�.txt")
    train.train("D://project/Aiwork/data_set/2016-10.txt")
    transfer.proccess_transfer_list("D://project/Aiwork/lib/ƴ�����ֱ�.txt")
    init_emission()
    for key in transfer.py:
        for word in transfer.py[key]:
            print(key, transfer.py[key][word])