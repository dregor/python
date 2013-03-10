
class Arch():

    def __init__( self, name, path = None ):
        from os import path
        from multiprocessing import Queue, Process
        self.name = name
        self.queue_file = Queue()
        if path == None:
            self.path = path.dirname( __file__ )
        else:
            self.path = path
        self.runing = True
        self.process_list = Process

    def __str__(self):
        return self.name

    def stop( self ):
        self.run = False

    def execute( self ):
        while true:
            try:
                file_name = self.queue_file.get( block = True )
            except queue_file.Empty:
                os._exit()
            else:
                arch_desc.extract( file_name )


    def get_queue( self ):
        i = 0
        for i in range( self.queue_file.qsize().__int__() ):
            print( self.queue_file.get( block=False ) )



class ZipArch( Arch ):
    def __init__( self, name, path = None ):
        from zipfile import ZipFile
        Arch.__init__( self, name , path )
        self.arch_desc = ZipFile( name, 'r' )
        for item in self.arch_desc.namelist():
            self.queue_file.put( item )

class RarArch( Arch ):
    def __init__( self, name, path = None ):
        from rarfile import RarFile
        Arch.__init__( self, name , path )
        self.arch_desc = RarFile( name, 'r' )
        for item in self.arch_desc.namelist():
            self.queue_file.put( item )

class TarArch( Arch ):
    def __init__( self, name, path = None ):
        import tarfile
        Arch.__init__( self, name , path )
        if name[-7:] == '.tar.gz' : readstate = 'r:gz'
        elif name[-8:] == '.tar.bz2' :  readstate = 'r:bz2'
        else : readstate = 'r:tar'
        self.arch_desc = tarfile.open( name , readstate )
	for item in self.arch_desc.getmembers:
            self.queue_file.put( item.name )


