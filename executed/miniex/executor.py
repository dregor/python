

class Arch():

    def __init__( name, path = None ):
        self.name = name
        if path = None:
            self.path = os.path.dirname( __file__ )
        else:
            self.path = path

    def __str__(self):
        return self.name

    def exec( arch_desc, queue_file ):
        while True:
            try:
                file_name = self.queue_file.get( block = True )
            except queue_file.Empty:
                pass
            else:
                arch_desc.extract( file_name )


class ZipArch( Arch ):
    def __init__( name, path = None )

