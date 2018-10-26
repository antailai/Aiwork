# coding:gbk
'''
  ����ȡ����ƴ��ת���ɺ����б�
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
    hanzi = open("../lib/һ�������ֱ�.txt").read()
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
        tmp = line.split(" ")  # ��ÿ��ƴ���ֿ�д��list
        for item in tmp:  # ����ÿ��ƴ��
            for tmp_spell in py:
                if tmp_spell.pinyin == item:
                    # ����ƴ����Ӧ�Ķ���
                    tmp_sentence.append(tmp_spell.pinyin2word())
    return tmp_sentence


# if __name__ == '__main__':
#     py = proccess_transfer_list("../lib/ƴ�����ֱ�.txt")
#     sentence = transfer("../data/input.txt")
#     for word_list in sentence:
#         print(''.join(word_list))
