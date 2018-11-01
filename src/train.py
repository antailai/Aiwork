# coding:utf-8
'''
  语料库中读取到的正文进行训练
'''
import load
import jieba
import time

# import pypinyin


def cut(s):
    return jieba.cut(s, cut_all=False)


def isChinese(s):
    for each_char in s:
        if '\u4e00' <= each_char <= '\u9fff':
            return True
        return False


def is_not_empty(s):
    return s and len(s.strip()) > 0


def train(data_set_path):
    # 现在这样处理不能处理多音字，因为拼音和汉字对应的关系是在之后统计的，
    # 但是应该根据文本里的字的含义分析读音，从而去统计每个拼音对应的字的个数，
    # 现在这样只能统计不完全的字，很大的问题就是’了‘这个字
    text = load.load_dir(data_set_path)
    print('start train', end='')
    start_time = time.time()
    for i in range(len(text)):
        # tmp_pinyin = []
        # for item in cut(text[i]):
        #     tmp_pinyin.append(
        #         pypinyin.pinyin(
        #             item, style=pypinyin.Style.NORMAL, errors='ignore'))
        # for item in tmp_pinyin:
        #     for i in range(len(item)):
        #         if len(item[i]) == 1:
        #             item[i] = ''.join(item[i])
        #         else:
        #             for o in range(1, len(item[i])):
        #                 item[i][0] += item[i][o]
        #             item[i] = ''.join(item[i][0])
        # for item in tmp_pinyin:
        #     print(item)
        # text[i] = sub(r'[^\u4e00-\u9fa5]', ' ', text[i])
        # text[i] = text[i].split(' ')
        # text[i] = list(filter(is_not_empty, text[i]))
        cut_text = cut(text[i])
        cut_text = list(filter(lambda x: isChinese(x), cut_text))
        for item in cut_text:
            # if isChinese(item):
            for o in range(len(item)):
                if o != len(item) - 1:
                    tmp_word = item[o]
                    next_word = item[o + 1]
                    if tmp_word in load.wd:
                        if o == 0:
                            load.wd[tmp_word]['start_count'] += 1
                        load.wd[tmp_word]['count'] += 1
                        load.wd[tmp_word]['next_dict'].setdefault(next_word, 0)
                        load.wd[tmp_word]['next_dict'][next_word] += 1
                    else:
                        continue
                else:
                    tmp_word = item[o]
                    if tmp_word in load.wd:
                        load.wd[tmp_word]['count'] += 1
                    else:
                        continue
    end_time = time.time()
    print('totalcost', start_time - end_time)


if __name__ == '__main__':
    load.load_hanzi_list("D:/project/Aiwork/lib/一二级汉字表.txt")
    train("D:/project/Aiwork/data_set/2016-10.txt")
    for key in load.wd:
        if load.wd[key]['count'] != 0:
            print(key, load.wd[key])
