import _thread as thread, time

stdoutmutex = thread.allocate_lock() #  блокировка общего ресурса stdout 
numthr = 5 # Количество потоков
exitmutexes = [thread.allocate_lock() for i in range(numthr)] # блокировка завершения потока

def counter( myId, count, mutex ):
    for i in range(count):
        time.sleep( 1 / (myId+1) )
        with mutex:   # блок вывода и разблок по окончании
            print( '[%s] => %s' % ( myId, i ), time.time() )
    exitmutexes[myId].acquire() # процесс закончил работу - блокируем

for i in range(numthr):
    thread.start_new_thread(counter, ( i, 5, stdoutmutex )) # запускаем процессы 

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
# Проверяем заблокированы ли процессы - если нет то ждемс

print('Основной поток завершен.')
