# -*- coding: utf-8 -*-
# @Time: 2022/1/25 9:16 AM
# @Author: wangpengpeng
# @Version: first
# @ Function:

import os
from .utils.check_method import check_read, check_write
class HandleFile:


    def check_file(self, file_name):
        if not os.path.isfile(file_name):
            print('{} is not exit'.format(file_name))
            exit()

    def check_dir(self, file_name):
        file_path = os.path.dirname(file_name)
        if not os.path.isdir(file_path):
            print('{} is not exit'.format(file_path))
            exit()

    def read_method(self, **kwargs):
        pass


    def write_method(self, **kwargs):
        pass