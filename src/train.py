# coding:gbk
'''
  ���Ͽ��ж�ȡ�������Ľ���ѵ��
'''
import load
import re
# import jieba


# def cut(s):
#     return jieba.cut(s, cut_all=False)
    

def train(data_set_path):
    # ���ı�˼·��ÿ�����Ӳ�ֱ�Ӵ�����jieba�ȷִʣ����ֺõĴ�ֱ��ת��Ϊpinyin������wd���dict�������е����ݶ�����pinyin���档
    text = load.load_dir(data_set_path)
    for i in range(len(text)):
        text[i] = re.sub(r'[^\u4e00-\u9fa5]', '', text[i])
        # cut(text[i])
        for o in range(len(text[i])):
            if o != len(text[i]) - 1:
                tmp_word = text[i][o]
                next_word = text[i][o + 1]
                if tmp_word in load.wd:
                    load.wd[tmp_word]['count'] += 1
                    load.wd[tmp_word]['next_dict'].setdefault(next_word, 0)
                    load.wd[tmp_word]['next_dict'][next_word] += 1
                else:
                    continue
            else:
                tmp_word = text[i][o]
                if tmp_word in load.wd:
                    load.wd[tmp_word]['count'] += 1
                else:
                    continue


# if __name__ == '__main__':
#     load.load_hanzi_list("../lib/һ�������ֱ�.txt")
#     train("../data_set/2016-10.txt")
#     for key in load.wd:
#         if load.wd[key]['count'] != 0:
#             print(key, load.wd[key])
