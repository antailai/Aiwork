# coding:utf-8
'''
  语料库中读取到的正文进行训练
'''
import load
import re
import jieba
import pypinyin


def cut(s):
    return jieba.cut(s, cut_all=False)


# def isChinese(s):
#     for each_char in s:
#         if '\u4e00' <= each_char <= '\u9fff':
#             return True
#         return False


def train(data_set_path):
    # 待改变思路，每个句子不直接处理，用jieba先分词，将分好的词直接转换为pinyin，不用wd这个dict，把所有的数据都存在pinyin里面。
    text = load.load_dir(data_set_path)
    for i in range(1):
        tmp_pinyin = []
        text[i] = re.sub(r'[^\u4e00-\u9fa5]', '', text[i])
        for item in cut(text[i]):
            tmp_pinyin.append(
                pypinyin.pinyin(
                    item, style=pypinyin.Style.NORMAL, errors='ignore'))
        for item in tmp_pinyin:
            for i in range(len(item)):
                if len(item[i]) == 1:
                    item[i] = ''.join(item[i])
                else:
                    for o in range(1, len(item[i])):
                        item[i][0] += item[i][o]
                    item[i] = ''.join(item[i][0])
        # for o in range(len(text[i])):
        #     if o != len(text[i]) - 1:
        #         tmp_word = text[i][o]
        #         next_word = text[i][o + 1]
        #         if tmp_word in load.wd:
        #             load.wd[tmp_word]['count'] += 1
        #             load.wd[tmp_word]['next_dict'].setdefault(next_word, 0)
        #             load.wd[tmp_word]['next_dict'][next_word] += 1
        #         else:
        #             continue
        #     else:
        #         tmp_word = text[i][o]
        #         if tmp_word in load.wd:
        #             load.wd[tmp_word]['count'] += 1
        #         else:
        #             continue


if __name__ == '__main__':
    # load.load_hanzi_list("../lib/一二级汉字表.txt")
    train("../data_set/2016-10.txt")
    # for key in load.wd:
    #     if load.wd[key]['count'] != 0:
    #         print(key, load.wd[key])
