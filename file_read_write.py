"""
author: xzshi19
aims: file operator
date: 2019.09.01
"""
import time
from math import sqrt
import json
import requests


def file5():
    my_dict = {
        'name': 'shi',
        'age': '23',
        'wei_xin': 'sxz136143',
        'friends': 'milk',
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 240}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(my_dict, fs)
    except IOError as e:
        print(e)
    print('save finished!')


class FileReadWrite(object):

    def __init__(self, name, num):
        self._name = name
        self._num = num

    def file1(self):
        f = None
        try:
            f = open(self._name, 'r', encoding='utf-8')
            print(f.read())
        except FileNotFoundError:
            print('file not found!')
        except LookupError:
            print('Look up error!')
        except UnicodeDecodeError:
            print('decode error')
        finally:
            if f:
                f.close()
        # 因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作

    def file2(self):
        try:
            with open(self._name, 'r', encoding='utf-8') as f:
                print(f.read())
        except FileNotFoundError:
            print('file not found')
        except UnicodeDecodeError:
            print('decode error')

    def file3(self):
        with open(self._name, 'r', encoding='utf-8') as f:
            print(f.read())

        with open(self._name, mode='r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
        print()

        with open(self._name) as f:
            lines = f.readlines()
        print(lines)

    def is_prime(self):
        '''判断素数的函数'''
        assert self._num > 0
        for factor in range(2, int(sqrt(self._num)) + 1):
            if self._num % factor == 0:
                return False
        return True if n != 1 else False

    def file4(self):
        try:
            with open(self._name, 'rb') as fs1:
                data = fs1.read()
                print(type(data))
            with open(self._name, 'wb') as fs2:
                fs2.write(data)
        except FileNotFoundError as e:
            print('no such file')
        except IOError as e:
            print('read or write error!')
        print('process end')

    # dump - 将Python对象按照JSON格式序列化到文件中
    # dumps - 将Python对象处理成JSON格式的字符串
    # load - 将文件中的JSON数据反序列化成对象
    # loads - 将字符串的内容反序列化成Python对象

    def file6(self):
        resp = requests.get(str(self._name))
        data_model = json.loads(resp.text)
        for news in data_model['newlist']:
            print(news['title'])
