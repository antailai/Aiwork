# coding:gbk
'''
  将读取到的拼音转换成汉字列表
'''
import re

py = list()


class spell:
    def __init__(self, pinyin, word):
        self.pinyin = pinyin
        self.word = word

    def pinyin2word(self):
        return self.word

    def display(self):
        print(self.pinyin)
        print(self.word)


def proccess_transfer_list(pinyin2hanzi_path):
    pinyin2hanzi = open(pinyin2hanzi_path)
    hanzi = open("../lib/一二级汉字表.txt").read()
    for line in pinyin2hanzi.readlines():
        line = re.sub('\n', '', line)
        tmp = line.split(" ")
        tmp_pinyin = tmp[0]
        tmp_word = []
        for i in range(1, len(tmp)):
            if tmp[i] in hanzi:
                tmp_word.append(tmp[i])
        tmp_py = spell(tmp_pinyin, tmp_word)
        py.append(tmp_py)
    return py


def transfer(input_path):
    input = open(input_path)  # open the input.txt
    tmp_sentence = []
    for line in input.readlines():
        tmp = line.split(" ")  # 将每个拼音分开写进list
        for item in tmp:  # 处理每个拼音
            for tmp_spell in py:
                if tmp_spell.pinyin == item:
                    # 查找拼音对应的对象
                    tmp_sentence.append(tmp_spell.pinyin2word())
    return tmp_sentence


# if __name__ == '__main__':
#     py = proccess_transfer_list("../lib/拼音汉字表.txt")
#     sentence = transfer("../data/input.txt")
#     for word_list in sentence:
#         print(''.join(word_list))
