def a( queue, arch ):
    import os
    while not queue.empty():
        file = queue.get( block = True )
        print( file + ' - ' + os.getpid().__str__() )
        arch.extract( file )

class Exed():

    def __init__( self, name, path = None, proc = None):
        from multiprocessing import Queue, Process, Pool, Manager, cpu_count
        from executor import TarArch, RarArch, ZipArch

        if name[-8:] == '.tar.bz2' or name[-4:] == '.tar' or name[-7] == '.tar.gz':
            self.arch = TarArch( name )
        elif name[-4:] == '.zip':
            self.arch =ZipArch( name )
        elif name[-4:] == '.rar':
            self.arch = RarArch( name )

        m = Manager()
        self.queue = m.Queue()

        for item in self.arch.name_list():
            self.queue.put( item )

        #self.pool = Pool( processes = 4 )

        if proc == None:
            self.proc = cpu_count()
        else:
            self.proc = proc

        self.proc_list = []

        for item in range( self.proc ):
            self.proc_list.append( Process(target=a, args=(self.queue,self.arch)) )

    def stop( self ):
        self.runing = False
        for item in self.proc_list:
            item.terminate()

    def start( self):
        #import pdb
        #pdb.set_trace()
        self.runing = True
        #self.pool.apply_async( a, args = ( self.queue , self.arch))
        for item in self.proc_list:
            item.start()
            print(item)

