# -*- coding: utf-8 -*-
# @Time: 2022/1/25 9:15 AM
# @Author: wangpengpeng
# @Version: first
# @ Function:

from handle_method.handlefile_inference import *
import json

class HandleTxt(HandleFile):

    def __init__(self):
        super().__init__()

    def read_method(self, file_name):
        '''
        :param file_name: 目标文件
        :return: 返回一个dic文件
        '''
        self.check_file(file_name)
        with open(file_name, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def write_method(self, dst_file, contents):
        '''
        :param dst_file: 目标文件
        :param contents: dic类型
        :return: 返回 T/F 提示对文件进行写入完成
        '''
        self.check_dir(dst_file)
        try:
            with open(dst_file, "w") as f:
                json.dump(contents, f)
            return True
        except Exception as e:
            print(e)
            return False

