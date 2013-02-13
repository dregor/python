#! /usr/bin/env python3
import sys,pickle,io,argparse

class Persons:

    def __init__(self,PersonList = []):
        self.PersonList = PersonList

    def save(self,Person = None):
        if Person is None:
            Person = self.PersonList[0]
        try:
            file = io.open(Person.name+'.bsa','wb')
        except:
            result = 'Не записано'
        else:
            pickle.dump(Person,file)
            file.close()
            result = str( file )+' \n- Записано в - '+Person.name+'.bsa'
        finally:
             return result

    def read(self,filename):
        file = io.open(filename,'rb')
        self.PersonList.append(pickle.load(file))
        file.close()

    def append(person):
        self.PersonList.append(person)


class Person:
    def __init__(self, name, age, pay=0, job='None'):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

    def __str__(self):
        a  = '\n========Персона========\n'
        a += (str( self.__class__ ))+'\n\nИмя -'+self.name
        a += '\nВозраст -'+self.age
        a += '\nЗарплата -'+str(self.pay)
        a += '\nРабота -'+self.job
        a += '\n========*******========\n'
        return a

if __name__ == '__main__':
    man=None
    parser = argparse.ArgumentDefaultsHelpFormatter(description('Аргументы'))
    print( 'Параметров -',str(len(sys.argv) ) )
    
    if( len(sys.argv)==1 ):
        sys.argv=['class.py','Jhon_Smith','24',10000,'worker']
    if( len(sys.argv)==2 ):
        print('В разработке!')
    elif( len(sys.argv)==3 ):
        man = Person( sys.argv[1], sys.argv[2] )
    elif( len(sys.argv)==4 ):
        man = Person( sys.argv[1], sys.argv[2], sys.argv[3]  )
    elif( len(sys.argv)==5 ):
        man = Person( sys.argv[1], sys.argv[2] , sys.argv[3] , sys.argv[4] )
    else:
        print('Добавте параметры: name age [pay] [job] .')
    if man is not None:
        print(man)
        PL = Persons([man])
        print(PL.save())

