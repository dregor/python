#! /usr/bin/env python3
from multiprocessing import Process, Pipe
import time,os

def f(conn):
    a = 'МОДУЛЬ : '+ __name__+ '\n'
    if hasattr(os, 'getppid'):
        a += 'РОДИТЕЛЬ : '+ str(os.getppid()) + '\n'
    a += 'id ПРОЦЕССА : '+ str(os.getpid()) + '\n'
    timeend = time.time()
    while time.time() < timeend + 10:
            a += 'СТЕК ВРЕМЕНИ : '+str(time.time())+'\n'
            time.sleep(1)
            conn.send(a)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p1 = Process(target=f, args=(child_conn,))
    p1.start()

    p2 = Process(target=f, args=(child_conn,))
    p2.start()

    timeend = time.time()
    while time.time() < timeend + 15:
        print('Время опроса:'+str(time.time()))
        print(parent_conn.recv())
        time.sleep(2)

    p1.terminate()
    p2.terminate()
