import os
print('\n현재 경로 :', os.getcwd())

try :
    ftest1 = open('../data/ftest.txt', mode = 'r')
    print(ftest1.read())

    ftest2 = open('../data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')

    ftest3 = open('../data/ftest2.txt', mode = 'a')
    ftest3.write('/nmy second text ~~~')

except Exception as e:
    print('Error 발생 : ', e)

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

try:
    ftest = open('../data/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('../data/ftest.txt', mode='r')
    lines = ftest.readline()
    print(lines)
    print(type(lines))
    print('문단 수 :', len(lines))

    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())

    print(docs)

    ftest = open('../data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
        print('Error 발생 : ', e)

finally:
        ftest.close()


