print('프로그램 시작 !!!')
x = [10, 30, 25.2, 'num', 14, 51]

for i in x :
    print(i)
    y = i**2
    print('y =', y)

print('프로그램 종료')

print('프로그램 시작!!!')

for i in x :
    try :
        y = i**2
        print('i=', i, 'y =', y)

    except :
        print('숫자 아님 : ', i)

print('프로그램 종료')

print('\n유형별 예외처리')
try :
    div = 1000 / 2.53
    print('div = %5.2f' %(div))
    div = 1000 / 0
    f = open('c:\\test.txt')
    num = int(input('숫자 입력 : '))

    print('num =', num)

except ZeroDivisionError as e:
    print('오류 정보 :', e)
except FileNotFoundError as e:
    print('오류 정보 :', e)
except Exception as e :
    print('오류 정보 : ', e)

finally:
    print('finally 영역 - 항상 실행되는 영역')

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