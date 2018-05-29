“只能计算pycharm下你打过的python代码行数，而且得把改文件放到PycharmProjects目录下才有用”

import os,re
R = 0
class Cal_PG:

    def __init__(self,current_path):
        self.current_path = current_path
        self.root_path = self.handle_root_path(current_path)
        self.handle_path(self.root_path)
        self.R = 0

    def handle_root_path(self,root_path):
        '获取PycharmProjects路径'

        while True:

            root_path_list = root_path.split('\\')
            if root_path_list[-1] =='PycharmProjects':
                return root_path
            else:
                root_path = os.path.dirname(root_path)

    def handle_path(self,path):
        '处理指定路径下的py文件发送给cal函数处理'


        file_list = os.listdir(path)
        for i in file_list:
            if  os.path.isdir(os.path.join(path,i)):
                if os.path.join(path,i) != os.path.join(path,'venv'): #venv目录是py内置文件不应计算行数

                    file_path = os.path.join(path,i)
                    self.handle_path(file_path)
            if re.findall(r'.py$',i):

                py_path = os.path.join(path,i)
                self.cal(py_path)

    def cal(self,py_path):
        global R
        print('py',py_path)
        with open(py_path, encoding='utf8') as f:
            data = f.readlines()
            r = len(data)

            R+=r

if __name__ == '__main__':
    Cal_PG(os.path.realpath(__file__))
    print('你曾经写过的代码行数',R)
