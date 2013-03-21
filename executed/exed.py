#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process

class ExedProc( Process ):
    def __init__( self, queue, arch ):
        Process.__init__( self )
        self.queue = queue
        self.arch = arch

    def run( self ):
        import os
        self.name += ' Exed '
        while not self.queue.empty():
            file = self.queue.get( block = True )
            self.arch.extract( file )
            self.name = os.getpid().__str__() +'  -  [' + file + ']'
            print( self.name )
        os._exit(0)


class Exed():

    def __init__( self, name, path = None, proc = None):
        from multiprocessing import Queue, cpu_count
        from executor import TarArch, RarArch, ZipArch
        import sys

        import logging as Log
        self.log = Log.getLogger()
        handlog = Log.StreamHandler( sys.stdout )
        handlog.setLevel( Log.DEBUG )
        handlog.setFormatter('%(asctime)s - %(levelname)s - %(process)d - %(processName)s - %(message)s')
        self.log.addHandler( handlog )
        self.log.info('Запуск распаковки %(name)s')

        if name[-8:] == '.tar.bz2' or name[-4:] == '.tar' or name[-7:] == '.tar.gz':
            self.arch = TarArch( name )
        elif name[-4:] == '.zip':
            self.arch =ZipArch( name )
        elif name[-4:] == '.rar':
            self.arch = RarArch( name )

        self.queue = Queue()

        for item in self.arch.name_list():
            self.queue.put( item )

        if proc == None:
            self.proc = cpu_count()
        else:
            self.proc = proc
        #self.proc = 1

        self.proc_list = [ ExedProc( self.queue, self.arch ) for item in range( self.proc )]

    def stop( self ):
        self.runing = False
        for item in self.proc_list:
            item.terminate()

    def start( self):
        self.runing = True
        for item in self.proc_list:
            item.start()
            print(item)

def is_alive( list ):
    for i in list:
        if i.is_alive():return True
    return False

if __name__ == '__main__':
    import os, sys, time
    test = Exed( os.path.dirname( __file__ ) + sys.argv[1] )
    test.start()

    while is_alive( test.proc_list ):
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            test.stop()
            print( 'Остановлено' )
