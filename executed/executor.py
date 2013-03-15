class Arch():

    def __init__( self, name, path = None ):
        from os import path
        self.name = name
        if path == None:
            self.path = path.dirname( __file__ )
        else:
            self.path = path

    def name_list( self ):
        return self.arch_desc.namelist()

    def __str__(self):
        return self.arch_desc.name

    def extract( self, file_name ):
           self.arch_desc.extract( file_name )


class ZipArch( Arch ):

    def __init__( self, name, path = None ):
        Arch.__init__( self, name , path )
        self.open()

    def open( self ):
        from zipfile import ZipFile
        self.arch_desc = ZipFile( self.name, 'r' )

    def __str__( self ):
        return self.arch_desc.filename

class RarArch( Arch ):

    def __init__( self, name, path = None ):
        Arch.__init__( self, name , path )
        self.open()

    def open( self ):
        from rarfile import RarFile
        self.arch_desc = RarFile( self.name, 'r' )

class TarArch( Arch ):

    def __init__( self, name, path = None ):
        Arch.__init__( self, name , path )
        self.open()

    def open( self ):
        import tarfile
        if self.name[-7:] == '.tar.gz' : readstate = 'r:gz'
        elif self.name[-8:] == '.tar.bz2' :  readstate = 'r:bz2'
        else : readstate = 'r:tar'
        self.arch_desc = tarfile.open( self.name , readstate )

    def name_list( self ):
        return [ i.name for i in self.arch_desc.getmembers() ]
