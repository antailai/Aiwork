# coding:gbk
'''
  将读取到的拼音转换成汉字列表
'''
import re

py = dict()


def proccess_transfer_list(pinyin2hanzi_path):
    pinyin2hanzi = open(pinyin2hanzi_path)
    hanzi = open("D://project/Aiwork/lib/一二级汉字表.txt").read()
    for line in pinyin2hanzi.readlines():
        line = re.sub('\n', '', line)
        tmp = line.split(" ")
        tmp_pinyin = tmp[0]
        tmp_dict = dict()
        for i in range(1, len(tmp)):
            if tmp[i] in hanzi:
                tmp_dict.setdefault(tmp[i], 0)
        py.setdefault(tmp_pinyin, tmp_dict)
    return py


def transfer(input_path):
    input = open(input_path)  # open the input.txt
    tmp_sentence = []
    for line in input.readlines():
        line = re.sub('\n', '', line)
        tmp = line.split(" ")  # 将每个拼音分开写进list
        for item in tmp:  # 处理每个拼音
            tmp_list = list()
            for key in py[item]:
                tmp_list.append(key)
            tmp_sentence.append(tmp_list)
    return tmp_sentence


# if __name__ == '__main__':
#     py = proccess_transfer_list("../lib/拼音汉字表.txt")
#     sentence = transfer("../data/input.txt")
#     for word_list in sentence:
#         print(''.join(word_list))
