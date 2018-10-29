# coding:gbk

import train
import transfer
import load


def init_emission():
    # qing->清：10 请：2 (for example) qing -> 清：10/12 请：2/12
    # wd[清] = {'word'= 清 'pinyin' = qing 'count' = 0 'next_dict' = {'华' = 10 '白' =5}}
    # py [qing] = (黥请顷庆倾檠轻氢卿磬罄鲭擎謦綮氰晴蜻圊清情箐苘亲青)
    for key in load.wd:
        transfer.py[load.wd[key]['pinyin']][key] = load.wd[key]['count']
    for key in transfer.py:
        sum = 0
        for word in transfer.py[key]:
            sum += transfer.py[key][word]
        for word in transfer.py[key]:
            transfer.py[key][word] /= sum


def init_tramsition():
    # wd[清] = {'word'= 清 'pinyin' = qing 'count' = 0 'next_dict' = {'华' = 10 '白' =5}} (for example) next_dict = {'华' = 10/15 '白' = 5/15}
    for key in load.wd:
        sum = 0
        for word in load.wd[key]['next_dict']:
            sum += load.wd[key]['next_dict'][word]
        for word in load.wd[key]['next_dict']:
            load.wd[key]['next_dict'][word] /= sum


if __name__ == '__main__':
    load.load_hanzi_list("D://project//Aiwork/lib/一二级汉字表.txt")
    train.train("D://project/Aiwork/data_set/2016-10.txt")
    transfer.proccess_transfer_list("D://project/Aiwork/lib/拼音汉字表.txt")
    init_emission()
    for key in transfer.py:
        for word in transfer.py[key]:
            print(key, transfer.py[key][word])