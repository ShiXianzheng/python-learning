"""
author ：xzshi19
aims: learning process and thread / multi
date: 2019.09.02
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('start download process, the id is %d' % getpid())
    print('now download %s ...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s finished, use %d seconds' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args='1.pdf')
    p1.start()
    p2 = Process(target=download_task, args='get.txt')
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('used %.2f seconds' % (end - start))


if __name__ == '__main__':
    main()
