import rarfile
arch = rarfile.RarFile("dir.rar")
for i in arch.namelist():
    print( i )
arch.extract( arch.namelist()[2] )
arch.close()
del( arch )
