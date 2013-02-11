#! /usr/bin/env python3
import os,sys,io

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

if __name__ == '__main__':
    print( 'Параметров -',str(len(sys.argv) ) )
    if( len(sys.argv)>3 ):
        man = Person( sys.argv[1], sys.argv[2] )
        print( str(man) + "\n" )
        print( "Имя -",man.name )
        print( "Возраст -",man.age )
        if(len(sys.argv)>4):
            man.pay = sys.argv[3]
        if(len(sys.argv)>5):
            man.pay = sys.argv[4]
        print( "Зарплата -",man.pay )
        print( "Работа -",man.job )
    else:
        print('Add men: name age [pay] [job] .')
