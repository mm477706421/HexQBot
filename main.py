
import time
import multiprocessing
import os

path=os.getcwd()

def thr1():
    os.system('python '+path+'/app/HexGame/post_api.py')

def thr2():
    os.system('python '+path+'/main_bot.py')


if __name__ == '__main__':
    start = time.time()

    p1 = multiprocessing.Process(target=thr1, )
    p2 = multiprocessing.Process(target=thr2, )

    # 启动子进程
    p1.start()
    p2.start()

    # 等待fork的子进程终止再继续往下执行，可选填一个timeout参数
    p1.join()
    p2.join()