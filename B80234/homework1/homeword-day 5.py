#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# 1. 读取文件
# ['aa', 'aaa-bbb-sds'] => ['aa', 'aaa', 'bbb', 'sds']
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list


def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")  # 打开文件
    lines = f.readlines()
    word_list = []
    for line in lines:
        line = line.strip()
        words = line.split(" ")  # 用空格分割
        words = word_split(words)  # 用-分割
        word_list.extend(words)
    return word_list


def get_file_from_folder(folder_path):  #获取文件夹里的所有路径
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


# 读取多文件里的单词
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path)) #用空格拆分单词后添加
    return final_words


# 2.获取格式化之后的单词
def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()


def format_words(words):
    word_list = []
    for word in words:
        wd = format_word(word)
        if wd:
            word_list.append(wd)
    return word_list


# 3. 统计单词数目
# {'aa':4, 'bb':1}
def statictcs_words(words):
    s_word_dict = {}
    for word in words:
        if s_word_dict.has_key(word):
            s_word_dict[word] = s_word_dict[word] + 1
        else:
            s_word_dict[word] = 1
    # 排序
    sorted_dict = sorted(s_word_dict.iteritems(), key=lambda d: d[1], reverse=True) #turple ((a,b),(b,c))
    return sorted_dict

def calculate_word(sorted_dict,total_count): #计算累积词频
    current_count = 0
    cal_list = {}
    for key in sorted_dict:
        num = key[1]
        word = key[0]
        current_count = current_count + num
        word_rate = float(current_count) / total_count
        cal_list[word] = round(word_rate,3)
    sortd_cal_list = sorted(cal_list.iteritems(), key=lambda d:d[0], reverse=False)
    return sortd_cal_list

def extract_word(sorted_cal_list,start,end):
    Flist = []#输入 [(a,b)]
    for length in range(len(sorted_cal_list)):
        if sorted_cal_list[length][1] > start and sorted_cal_list[length][1] < end:
            Flist.append(sorted_cal_list[length])
    return Flist
def read_file_A(file_path): #读取文件分割成list
    file = codecs.open(file_path,'r','utf-8')
    file_read = file.readlines()
    word_list = []
    for line in file_read:
        lines = line.strip()
        wd = lines.split('   ')
        word_list.append(wd)
    return word_list

def word_compare(word_list,Flist):
#对比截取的单词是否在8000里面
    word_table = {}
    for word in Flist:
        for meaning in word_list:
            if word[0] == meaning[0]:
                word_table[word[0]] = meaning[1]
                break
            else:
                word_table[word[0]] = 'no meaning'
    word_table = sorted(word_table.iteritems(),key=lambda d:d[0], reverse=False)
    return word_table
# 4.输出成csv
def print_to_csv(word_table, to_file_path ):
    nfile = open(to_file_path, 'w+')
    for val in word_table:
        nfile.write('%s,%s\n' % (val[0], val[1]))
    nfile.close()



def main():
    # 1. 读取文本
    words = read_files(get_file_from_folder('data1'))
    print '获取了未格式化的单词 %d 个' % (len(words))

    # 2. 清洗文本
    f_words = format_words(words)
    total_word_count = len(f_words)
    print '获取了已经格式化的单词 %d 个' % (len(f_words))

    # 3. 统计单词和排序
    word_list = statictcs_words(f_words)  #turple

    cal_list = calculate_word(word_list,total_word_count)

    extract_dict = extract_word(cal_list,0.5,0.7)

    word_list = read_file_A('8000-words.txt')
    word_table = word_compare(word_list,extract_dict)

    # 4. 输出文件
    print_to_csv(word_table, 'output/test-yang.csv')


if __name__ == "__main__":
    main()