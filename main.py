import time
import psutil
import os

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        stop = time.time()
        print('Время выполнения функции:', stop-start,'секунд')
    return wrapper




def memory(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        mem_1 = proc.memory_info().rss
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        mem_2 = proc.memory_info().rss
        print('Объем памяти:', mem_2 - mem_1, 'байт')
    return wrapper


n = 1000000

@timer
@memory
def list_num(n):
    list = [i for i in range(1,n+1)]
    return list

@timer
@memory
def gen_num(n):
    for i in range(1,n+1):
        yield(i)

list_num(n)
gen_num(n)

