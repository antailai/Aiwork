# coding:gbk

from train import train
from load import load_hanzi_list, load_pyhz_list, py, wd
import re
from time import process_time


class State:
    def __init__(self, sentence, probability):
        self.sentence = sentence
        self.probability = probability

    # def update_state(self, next_word):
    #     if next_word in wd[self.sentence[len(self.sentence) - 1]]['next_dict']:
    #         self.sentence.append(next_word)
    #         self.probability = self.probability * wd[self.sentence[
    #             len(self.sentence) - 1]]['next_dict'][next_word]
    #         return True
    #     else:
    #         return False


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


def init_transition():
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
                    start = py[tmp[i]][each_word]['start']
                    count = py[tmp[i]][each_word]['count']
                    start_probability = start * count
                    init_state = State(each_word, start_probability)
                    state_list.append(init_state)
            else:
                new_list = list()
                for each_word in py[tmp[i]]:
                    for each_state in state_list:
                        if each_word in wd[each_state.sentence[
                                len(each_state.sentence) - 1]]['next_dict']:
                            new_sentence = each_state.sentence + each_word
                            new_probability = each_state.probability * wd[
                                each_state.sentence[len(each_state.sentence) -
                                                    1]]['next_dict'][each_word]
                            new_state = State(new_sentence, new_probability)
                            new_list.append(new_state)
                state_list = new_list
        tmp_sentence.append(max(state_list, key=lambda x: x.probability))
        # for item in tmp_sentence:
        #     print(item)
    return tmp_sentence


if __name__ == '__main__':
    load_hanzi_list("D://project//Aiwork/lib/一二级汉字表.txt")
    load_hanzi_list_time = process_time()
    print('加载一二级汉字表总共花费了', load_hanzi_list_time, '秒')
    train("D://project/Aiwork/data_set")
    train_time = process_time()
    print('加载语料库与统计字频总共花费了', train_time - load_hanzi_list_time, '秒')
    load_pyhz_list("D://project/Aiwork/lib/拼音汉字表.txt")
    load_pyhz_list_time = process_time()
    print('加载拼音汉字表总共花费了', load_pyhz_list_time - train_time, '秒')
    init_start()
    start_time = process_time()
    # print('统计start总共花费了', start_time - load_pyhz_list_time, '秒')
    init_emission()
    emission_time = process_time()
    # print('统计emission总共花费了', emission_time - start_time, '秒')
    init_transition()
    transition_time = process_time()
    # print('统计transition总共花费了', transition_time - emission_time, '秒')
    tmp_sentence = transfer("D://project/Aiwork/data/input.txt")
    for sentence in tmp_sentence:
        print(sentence.sentence)
    # for key in transfer.py:
    #     for word in transfer.py[key]:
    #         print(word, transfer.py[key][word])
