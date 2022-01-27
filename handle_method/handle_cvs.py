# -*- coding: utf-8 -*-
# @Time: 2022/1/25 9:15 AM
# @Author: wangpengpeng
# @Version: first
# @ Function:

from handle_method.handlefile_inference import *
import csv

class HandleCsv(HandleFile):

    def __init__(self):
        super().__init__()

    @check_read
    def read_method(self, file_name):
        '''
        :param file_name: 目标文件
        :return: 返回一个数组, 第一行是标题
        '''
        with open(file_name, "r") as csvfile:
            reader = csv.reader(csvfile)
        return  reader

    @check_write
    def write_method(self, dst_file, titles, contents):
        '''

        :param dst_file: 目标文件
        :param titles: 内容的标题
        :param contents: list类型
        :return: 返回 T/F 提示对文件进行写入完成
        '''
        with open(dst_file, "w") as csvfile:
            writer = csv.writer(csvfile)
            # 先写入columns_name
            writer.writerow(titles)
            # 写入多行用writerows
            writer.writerows(contents)



