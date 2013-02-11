#! /usr/bin/env python3
import os,sys,io
if(len(sys.argv)==1):
    try:
        print( os.path.abspath(os.curdir)+'/text')
    except IOError:
        print('Нету файла')
        sys.exit()
    else:
        sys.argv.append(os.path.abspath(os.curdir)+'/text')
with io.open(sys.argv[1], 'r') as f:
    try:
        print(f)
        for line in f:
   print(line)
    except:
        print('ErrorReade')
    else:
        print('ReadeCompleate')

