# -*- coding: utf-8 -*-
# @Time: 2022/1/25 9:15 AM
# @Author: wangpengpeng
# @Version: first
# @ Function:

from handle_method.handlefile_inference import *

class HandleTxt(HandleFile):

    def __init__(self):
        super().__init__()

    def read_method(self, file_name):
        '''
        :param file_name: 目标文件
        :return: 返回一个数组文件
        '''
        self.check_file(file_name)
        return  open(file_name, 'r').readlines()

    def write_method(self, dst_file, contents):
        '''

        :param dst_file: 目标文件
        :param contents: list类型
        :return: 返回 T/F 提示对文件进行写入完成
        '''
        self.check_dir(dst_file)
        try:
            with open(dst_file, 'w') as dst_lines:
                for content in contents:
                    dst_lines.write(content + '\n')
            return True
        except Exception as e:
            print(e)
            return False

