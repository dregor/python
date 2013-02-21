import os,sys

print( __name__ )
print( __file__ )

dir = list( os.path.split( os.path.abspath( __file__ ) ) )[0]

print('this - '+dir)

for root, dirs, files in os.walk(dir): # пройти по директории рекурсивно
    for name in files:
            fullname = os.path.join(root, name) # получаем полное имя файла
            print(fullname)# делаем что-нибудь с ним
            print(root)
            print(dirs)
            print(files)
            print('_______')
