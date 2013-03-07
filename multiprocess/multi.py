
from multiprocessing import Process
import os

def info(title):
    print(title)
    print ('МОДУЛЬ : '+ __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print ('РОДИТЕЛЬ : '+ str(os.getppid()))
    print('id ПРОЦЕССА : '+ str(os.getpid()))

def f(name):
    info('Функция f')
    print('Имя - '+name)

if __name__ == '__main__':
    info('ГЛАВНЫЙ ПРОЦЕСС.')
    p = Process(target=f, args=('Егор',))
    p.start()
    p.join()
