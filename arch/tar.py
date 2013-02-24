import tarfile,sys
if len( sys.argv ) == 1 : sys.argv.append('dir.tar.bz2')
tarname = sys.argv[1]
if tarname[-7:] == '.tar.gz' : readstate = 'r:gz'
elif tarname[-8:] == '.tar.bz2' :  readstate = 'r:bz2'
else : readstate = 'r:tar'
print( 'Тип архива : ' + readstate )
print( "Имя архива : " + tarname )
tar = tarfile.open( tarname , readstate )
tar.list()
for tars in tar.members : print( tars.name )
#tar.extract(tar.members[2].name)
tar.close()

del( tar )
