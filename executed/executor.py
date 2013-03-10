class Arch():

    def __init__( self, name, path = None ):
        from os import path
        if path == None:
            self.path = path.dirname( __file__ )
        else:
            self.path = path

    def namelist( self ):
        return self.arch_desc.namelist()

    def __str__(self):
        return self.arch_desc.name

    def extract( self, file_name ):
           self.arch_desc.extract( file_name )

class ZipArch( Arch ):
    def __init__( self, name, path = None ):
        from zipfile import ZipFile
        Arch.__init__( self, name , path )
        self.arch_desc = ZipFile( name, 'r' )

    def __str__( self ):
        return self.arch_desc.filename

class RarArch( Arch ):
    def __init__( self, name, path = None ):
        from rarfile import RarFile
        Arch.__init__( self, name , path )
        self.arch_desc = RarFile( name, 'r' )

class TarArch( Arch ):
    def __init__( self, name, path = None ):
        import tarfile
        Arch.__init__( self, name , path )
        if name[-7:] == '.tar.gz' : readstate = 'r:gz'
        elif name[-8:] == '.tar.bz2' :  readstate = 'r:bz2'
        else : readstate = 'r:tar'
        self.arch_desc = tarfile.open( name , readstate )

    def namelist( self ):
        result = []
        for i in self.arch.getmembers():
            result.append( i.name )
        return result
