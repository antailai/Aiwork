# coding:gbk

from train import train
from load import load_hanzi_list, load_pyhz_list, py, wd
import re


class State:
    def __init__(self, sentence, probability):
        self.sentence = sentence
        self.probability = probability

    def update_state(self, next_word):
        self.sentence.append(next_word)
        self.probability = self.probability * wd[self.sentence[
            len(self.sentence) - 1]]['next_dict'][next_word]


def init_start():
    for key in wd:
        py[wd[key]['pinyin']][key]['start'] = wd[key]['start_count']
    for key in py:
        sum = 0
        for word in py[key]:
            sum += py[key][word]['start']
        if sum == 0:
            continue
        for word in py[key]:
            py[key][word]['start'] /= sum


def init_emission():
    for key in wd:
        py[wd[key]['pinyin']][key]['count'] = wd[key]['count']
    for key in py:
        sum = 0
        for word in py[key]:
            sum += py[key][word]['count']
        if sum == 0:
            continue
        for word in py[key]:
            py[key][word]['count'] /= sum


def init_tramsition():
    for key in wd:
        sum = 0
        for word in wd[key]['next_dict']:
            sum += wd[key]['next_dict'][word]
        for word in wd[key]['next_dict']:
            wd[key]['next_dict'][word] /= sum


def transfer(input_path):
    # py [qing] = {'清' = 10 '青' =5}
    # 实现viterbi算法
    input = open(input_path)  # open the input.txt
    tmp_sentence = []
    for line in input.readlines():
        state_list = []
        line = re.sub('\n', '', line)
        tmp = line.split(" ")  # 将每个拼音分开写进list
        for i in range(len(tmp)):  # 处理每个拼音
            if i == 0:
                for each_word in py[tmp[i]]:
                    start_probability = py[tmp[i][each_word]]['start'] * py[
                        tmp[i]][each_word]['count']
                    init_state = State(each_word, start_probability)
                    state_list.append(init_state)
            for each_word in py[tmp[i]]:
                for each_state in state_list:
                    each_state.update_state(each_word)

        tmp_sentence.append(max(state_list, key=lambda x: x.probability))
    return tmp_sentence


if __name__ == '__main__':
    load_hanzi_list("D://project//Aiwork/lib/一二级汉字表.txt")
    train("D://project/Aiwork/data_set")
    load_pyhz_list("D://project/Aiwork/lib/拼音汉字表.txt")
    init_start()
    init_emission()
    init_tramsition()
    tmp_sentence = transfer("D://project/Aiwork/data/input.txt")
    for sentence in tmp_sentence:
        print(sentence)
    # for key in transfer.py:
    #     for word in transfer.py[key]:
    #         print(word, transfer.py[key][word])
