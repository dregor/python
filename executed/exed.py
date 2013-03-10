def a( q, obj ):
    while not queue.empty():
        f = q.get( block = True )
        obj.extract( f )

class Exed():

    def __init__( self, name, path = None ):
        from multiprocessing import Queue, Pool, Manager
        from executor import TarArch, RarArch, ZipArch

        if name[-8:] == '.tar.bz2' or name[-4:] == '.tar' or name[-7] == '.tar.gz':
            self.arch = TarArch( name )
        elif name[-4:] == '.zip':
            self.arch =ZipArch( name )
        elif name[-4:] == '.rar':
            self.arch = RarArch( name )
        m = Manager()
        self.queue = m.Queue()
        self.pool = Pool( processes = 4 )

    def stop( self ):
        self.runing = False

    def start( self):
        import pdb
        pdb.set_trace()
        self.runing = True
        self.pool.apply_async( a, args = ( self.queue , self.arch))

