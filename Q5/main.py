import os

def create_dir(name , address):
    path = os.path.join(address ,name)
    if os.path.exists(path):
        print('Directory already exist')
    else:
        os.mkdir(path)
        print('Directory created')
        
def create_file(name ,address):
    path = os.path.join(address ,name)
    if os.path.isfile(path):
        print('file already exist')
    else:
        open(path, 'a').close()
        print('file created')
        

def delete(name ,address):
    path = os.path.join(address ,name)
    if os.path.isfile(path):
        os.remove(path)
        print('file deleted')
    else:
        print('file didnt exsit')
        
def find(name ,address):
    files = list()
    for file in os.listdir(address):
        if name in file:
            path = os.path.join(address , file)
            files.append(path)
    return files
    

create_dir('AP_hw' ,os.getcwd())

create_file('main.cpp' ,os.path.join(os.getcwd(),'AP_hw'))
create_file('main.h' ,os.path.join(os.getcwd(),'AP_hw'))
create_file('main.o' ,os.path.join(os.getcwd(),'AP_hw'))
create_file('main.py' ,os.path.join(os.getcwd(),'AP_hw'))
create_dir('main' ,os.path.join(os.getcwd(),'AP_hw'))

delete('main.py' ,os.path.join(os.getcwd(),'AP_hw'))

print('\n'.join(find('main',os.path.join(os.getcwd(),'AP_hw') )))
