# -*- coding: utf-8 -*-
# @Time: 2022/1/25 2:03 PM
# @Author: wangpengpeng
# @Version: first
# @ Function:

import handle_method

def wrapper(self):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print('读方法参数：', self.operate_method.read_method.__doc__)
            print('写方法参数：', self.operate_method.write_method.__doc__)
            # 默认的读取方式是使用 传入的方法；可以自行指定
            try:
                print('正在使用的文件为：', kwargs['file_name'])
            except:
                kwargs['file_name'] = self.file_name
            return func(*args, **kwargs)
        return wrapper
    return outwrapper



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


    def read_method(self, **kwargs):
        '''
        文件读取的格式；
        :param kwargs:
        :return:
        '''
        print('函数的使用方法：', self.operate_method.read_method.__doc__)
        # 默认的读取方式是使用 传入的方法；可以自行指定
        try:
            print('正在使用的文件为：', kwargs['file_name'])
        except:
            kwargs['file_name'] = self.file_name
        return self.operate_method.read_method(**kwargs)

    def write_method(self, **kwargs):
        '''
        文件的写入方式
        :param kwargs:
        :return:
        '''
        print('函数的使用方法：', self.operate_method.write_method.__doc__)
        try:
            print('正在使用的文件为：', kwargs['file_name'])
        except:
            kwargs['file_name'] = self.file_name

        self.operate_method.write_method(**kwargs)



if __name__ == '__main__':
    file_name= 'data1.xlsx'
    open_test = OperateFile(file_name)
    method_test = open_test.read_method() #file_name=file_name
    # print(open_test.read_method.__doc__)

