# -*- coding: utf-8 -*-
# @Time: 2022/1/25 2:03 PM
# @Author: wangpengpeng
# @Version: first
# @ Function:

import handle_method



def prepare(func):
    def wrapper(self, **kwargs):
        func_name = func.__name__
        doc_func= getattr(self.operate_method, func_name).__doc__
        print('参数介绍：', doc_func)

        if kwargs.get('file_name', None) is None:
            kwargs['file_name'] = self.file_name
        return func(self, **kwargs)
    return wrapper

class OperateFile:

    def __init__(self,file_name):
        self.file_name = file_name
        self.operate_method = self.get_method()

    def get_method(self):

        file_suffix = self.file_name.split('.')[-1]

        try:
            file_suffix = file_suffix[0].upper() + file_suffix[1:]
        except:
            print('文件后缀名错误')
            exit()

        operate_method = getattr(handle_method, 'Handle{}'.format(file_suffix))
        return operate_method()



    @prepare
    def read_method(self, **kwargs):
        '''
        文件读取的格式；
        :param kwargs:
        :return:
        '''
        return self.operate_method.read_method(**kwargs)

    @prepare
    def write_method(self, **kwargs):
        '''
        文件的写入方式
        :param kwargs:
        :return:
        '''
        self.operate_method.write_method(**kwargs)



if __name__ == '__main__':
    file_name= 'data1.xlsx'
    open_test = OperateFile(file_name)
    method_test = open_test.read_method() #file_name=file_name
    # print(open_test.read_method.__doc__)

