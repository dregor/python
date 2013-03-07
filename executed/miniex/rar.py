def rarexec( arch_desc, queue_file ):
    while True:
        try:
            file_name = queue_file.get( block = True )
        except queue_file.Empty:
            pass
        else:
            print( file_name )
            arch_desc.extract( file_name )


