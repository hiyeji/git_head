# 문자열 유형
oneline = 'this is one line string'
print(oneline)

multiline = '''this is
multi line
string'''
print(multiline)

multiline2 = 'this is\nmulti line\nstring'
print(multiline2)

# (1) 문자열 색인
string = 'PYTHON'
print(string[0])
print(string[5])
print(string[-1])
print(string[6])

# (1) 문자열 연산
print('python' + ' program')  # 결합연산자
print('python-' + str(3.7) + '.exe')  # python-3.7.exe
print('-' * 30)  # 반복연산자

# (1) 왼쪽 기준
print(oneline)
print('문자열 길이 : ', len(oneline) )
print(oneline[0 : 4])
print(oneline[:4])
print(oneline[:])
print(oneline[::2])

# (2) 오른쪽 기준
print(oneline[0:-1:2])
print(oneline[-6:-1])
print(oneline[-6:])

# (1) 특정글자 수 반환
oneline = 'this is one line string'
print('t 글자 수 : ', oneline.count('t'))

# (2) 접두어 문자 비교 판단
print(oneline.startswith('this'))
print(oneline.startswith('that'))

# (3) 문자열 교체
print(oneline.replace('this', 'that'))

# (4) 문자열 분리(split) " 문단-> 문장
multiline = """ this is 
multi line
string"""
sent = multiline.split('\n')
print('문장 : ', sent)

# (5) 문자열 분리(split) " 문장-> 단어
words = oneline.split(' ')
print('단어 :', words)

# (6) 문자열 결합(join) : 단어 -> 문장
sent2 = ','.join(words) # '구분자'.join(string)
print(sent2) # this,is,one,line,string

