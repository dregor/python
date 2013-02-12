#! /usr/bin/env python3
import sys

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

if __name__ == '__main__':
    print( 'Параметров -',str(len(sys.argv) ) )
    man=None

    if( len(sys.argv)==2 ):
        print('Эта часть пока не готова')
    elif( len(sys.argv)==3 ):
        man = Person( sys.argv[1], sys.argv[2] )
    elif( len(sys.argv)==4 ):
        man = Person( sys.argv[1], sys.argv[2], sys.argv[3] )
    elif( len(sys.argv)==5 ):
        man = Person( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )
    else:
        print('Добавте параметры: name age [pay] [job] .')

    if(man is not None):
        print( str(man) + "\n" )
        print( "Имя -",man.name )
        print( "Возраст -",man.age )
        print( "Зарплата -",man.pay )
        print( "Работа -",man.job )
