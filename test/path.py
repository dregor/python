
import os

print("Имя текущего модуля "+ __name__ )


print( "Имя скрипта "+ __file__ )

d = os.path.dirname( os.path.abspath( __file__ ) )


print( 'Текущая директория ' +  d  )

for root, dirs, files in os.walk( d ): # пройти по директории рекурсивно
    for name in files:
            fullname = os.path.join( root, name )  # получаем полное имя файла
            print("Полное имя " + fullname )# делаем что-нибудь с ним
            print("Рут " + root )
            print("Директории " + str(dirs) )
            print("Файлы " + str(files) )
            print('_______')

print('\nGlobal тест')
from glob import *
import re

for i in iglob('/*'):
    if re.findall('.*bin|.*usr',i):
        print( i )

print( glob('*.py') )
print('\n')
[print(a) for a in iglob('/*') if re.search('.*bin',a) != None]

