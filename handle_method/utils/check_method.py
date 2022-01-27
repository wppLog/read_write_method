# -*- coding: utf-8 -*-
# @Time: 2022/1/26 9:03 AM
# @Author: wangpengpeng
# @Version: first
# @ Function:
def check_read(func):
    def wrapper(self, **kwargs):
        self.check_file(kwargs['file_name'])
        try:
            print('参数介绍', func.__doc__)
            func(self, **kwargs)
            print('数据读取成功！')
        except Exception as e:
            print(e)
            exit()
        return func(self,**kwargs)
    return wrapper




def check_write(func):
    def wrapper(self, **kwargs):
        self.check_dir(kwargs['dst_file'])

        try:
            print('参数介绍', func.__doc__)
            func(self, **kwargs)
            print('数据写入成功')
        except Exception as e:
            print(e)
            exit()
        return func(self,**kwargs)
    return wrapper

