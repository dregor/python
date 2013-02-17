#! /usr/bin/env python3
import os,re
from zipfile import ZipFile

curdir =  os.path.split( os.path.abspath(__file__) )[0] #Текущая директория

zin = ZipFile(curdir+'/dir.zip', 'r')
zout = ZipFile(curdir+'/dir2.zip', 'w')
for item in zin.infolist():
    buf = zin.read(item.filename)
    if re.findall( '(.*testfile1)', item.filename ) != [] :
        print(item.filename)
        zout.writestr(item, buf)
zout.close()
zin.close()
