# coding:gbk
'''
  ���Ͽ��ж�ȡ�������Ľ���ѵ��
'''
import load
import re


def train(data_set_path):
    text = load.load_dir(data_set_path)
    for i in range(0, 1):
        text[i] = re.sub(r'[^\u4e00-\u9fa5]', '', text[i])
        for o in range(len(text[i])):
            if o != len(text[i]) - 1:
                tmp_word = text[i][o]
                next_word = text[i][o + 1]
                load.wd[tmp_word]['count'] += 1
                if next_word in load.wd[tmp_word]['next_dict']:
                    load.wd[tmp_word]['next_dict'][next_word] += 1
                else:
                    load.wd[tmp_word]['next_dict'][next_word] = 1
            else:
                tmp_word = text[i][o]
                load.wd[tmp_word]['count'] += 1


if __name__ == '__main__':
    load.load_hanzi_list("../lib/һ�������ֱ�.txt")
    train("../data_set/p2016-10.txt")
    for key in load.wd:
        if load.wd[key]['count'] != 0:
            print(key, load.wd[key])
