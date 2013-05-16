#! /usr/bin/env python3
import os, io,pickle, argparse

class Persons:
    ''' Класс для работы со списком персон.
        Отображает,сохраняет в файл,считывает.
    '''

    def __init__( self, dir, PersonList = [] ):
        self.rootdir = dir
        self.PersonList = PersonList

    def save( self, Person = None ):
        ''' Сохраняет конкретную персону в файл.
        '''
        if Person is None:
            Person = self.PersonList[0]
        try:
            file = io.open( os.path.join(self.rootdir,(Person.name+'.bsa')),'wb')
        except:
            result = 'Не записано'
        else:
            pickle.dump( Person, file )
            file.close()
            result = str( file )+' \n- Записано в - '+Person.name+'.bsa'
        finally:
            return result

    def save_all( self ):
        ''' Сохраняет все персоны из списка в файлы.
        '''
        a=[]
        for p in self.PersonList:
            a.append(self.save(p))
        return a

    def read( self, file ):
        ''' Считывает персону из указанного файла.
        '''
        man= pickle.load(file)
        result  =  'Загружено из : '
        result +=  str(file) + '\n\n' + str(man)
        self.append(man)
        file.close()
        return result

    def read_all( self, path = None ):
        ''' Считывает все файлы из указанной директории
            (илииз директории по умолчанию)
        '''

        if (path == None):
            path = self.rootdir
        for ( root, dirs, files ) in os.walk(path):
            for name in files:
                fullname = os.path.join( root, name )
                if (fullname[-4:]=='.bsa'):
                    file = io.open( fullname, 'rb' )
                    self.read(file)
        return self.show_all()


    def show_all(self):
        ''' Возвращает список персон в текстовом виде.
        '''
        a=[]
        for p in self.PersonList:
            a.append(str(p))
        return a

    def append( self, person ):
        '''Добавляет персону в список.
        '''
        self.PersonList.append(person)

class Person:
    ''' Класс человек.
        Имя.
        Возраст.
        Зарплата.
        Работа.
    '''
    def __init__(self, name, age, pay=0, job='None'):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

    def __str__(self):
        a  = '\n========Персона========\n'
        a += ( str( self.__class__.__name__ ) )
        a += '\n\nИмя -'+self.name
        a += '\nВозраст - '+str( self.age )
        a += '\nЗарплата - '+str( self.pay )
        a += '\nРабота - '+self.job
        a += '\n========*******========\n'
        return a

class SuperPerson(Person):
    ''' Класс супер-человека, наследник класса человек,
        плюс супер-способности.
    '''
    def __init__(self, name, age, pay=9999999, job='superhero',ability='fly'):
        Person.__init__(self,name,age,pay,job)
        self.ability=ability

    def __str__(self):
        a  = Person.__str__(self)
        a += '\nСуперспособности - '+self.ability
        a += '\n========*******========\n'
        return a


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Работа с персонами.')
    curdir =  os.path.dirname(__file__)  #Текущая директория
    #Работа с параметрами командной строки

    subparsers = parser.add_subparsers(help='Варианты работ:', dest='vary')
    add_parser = subparsers.add_parser('create', help='Создание.')
    add_parser.add_argument('-s', '--super',
                            default=None,
                            dest='super',
                            help='СуперХерой, после ключа абилитис')
    add_parser.add_argument('name', help='Имя')
    add_parser.add_argument('age', type=int, help='Возраст')

    add_parser.add_argument('-p','--pay', type=int,
                            default=None,
                            dest='pay', help='Зарплата')
    add_parser.add_argument('-j','--job', default=None,
                            dest='job', help='Работа')
    add_parser.set_defaults(which='create')

    load_parser = subparsers.add_parser('load',help='Загрузить.')
    load_parser.add_argument('file',
                            type = argparse.FileType('rb'),
                            nargs='*', default=None,
                            help='Файл')
    load_parser.add_argument('-a', '--all',
                            action='store_true',
                            dest='all',
                            default=False,
                            help='Все')
    load_parser.set_defaults(which='load')

    pars = parser.parse_args()

    #Реализация создания
    if( pars.vary == 'create' ):

        if( pars.super != None ):
            man = SuperPerson( pars.name, pars.age,ability = pars.super )
        else:
            man = Person( pars.name, pars.age )

        if( pars.pay != None ):
            man.pay =  pars.pay

        if( pars.job != None ):
            man.job = pars.job


        if man is not None:
            print(man)
            PL = Persons( curdir, [man] )
            for string in PL.save_all():
                print(string)
            del(man)

    #Реализация загрузки
    if ( pars.vary == 'load' ):
        if ( len(pars.file) > 0 and not pars.all ):
            for file in pars.file:
                PL = Persons( curdir )
                print( PL.read( file ) )
        elif ( pars.all and len(pars.file) == 0 ):
            PL = Persons( curdir )
            for string in  PL.read_all():
                print(string)
        else:
            print( 'Выбери, что-то одно. Или -а или filename.' )
