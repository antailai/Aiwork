# coding:gbk
'''
  语料库中读取到的正文进行训练
'''
import load
import re


def train(data_set_path):
    text = load.load_dir(data_set_path)
    for i in range(0, 5):
        text[i] = re.sub(r'[^\u4e00-\u9fa5]', '', text[i])
        for each_word in text[i]:
            for tmp_word in load.wd:
                if tmp_word.word == each_word:
                    next_word_count = tmp_word.next_data.setdefault(
                        tmp_word, 0)
                    next_word_count += 1
                    tmp_word.next_data[tmp_word] = next_word_count
                    tmp_word.count += 1


# list_cut = list(filter(is_space,list_cut))
# print(list_cut)
# f.close()

if __name__ == '__main__':
    load.load_hanzi_list(
        "D:\cloud\Seafile\project\python\AIwork-pinyin\lib\一二级汉字表.txt")
    train(
        "D:\cloud\Seafile\project\python\AIwork-pinyin\data_set\p2016-10.txt")
    for item in load.wd:
        if item.count != 0:
            print(item.word, end=' ')
            print(item.count, end=' ')
            print(item.pinyin, end=' ')
            print(item.next_data)
