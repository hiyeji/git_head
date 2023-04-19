import os
print('/n현재 경로 :', os.getcwd())

os.getcwd()

os.chdir('../Chapter08')
os.getcwd()

os.listdir('.')

os.mkdir('test')
os.listdir('.')

os.chdir('test')
os.getcwd()

os.makedirs('test2/test3')
os.listdir('.')

os.rmdir('test3')
os.listdir('.')

os.chdir('../..')
os.getcwd()

os.removedirs('test/test2')

import os.path
print('/n현재 경로 :', os.getcwd())

os.getcwd()

os.chdir('../Chapter08')
os.getcwd()

os.path.abspath('lecture/step01_try_except.py')

os.path.dirname('lecture/step01_try_except.py')

os.path.exists('D:\\Pywork\\workspace')

os.path.isfile('lecture/step01_try_except.py')

os.path.isdir('lecture')

os.path.split("c:\\test\\test1.txt")
os.path.join('c:\\test', 'test1.txt')

os.path.join('lecture/step01_try_except.py')

