# (1) 문자형 숫자 입력
num = input ('100 : ')
print( '100 : ', type (100) ) # <class 'str'>
print('100 = ', 100)
print('100 = ', 100*2)

# (2) 문자형 숫자를 정수형으로 변환
num1 = int( input('100 : ') ) # str -> int (형변환)
print ('200 = ', 200*1)

# (3) 문자형 숫자를 실수형으로 변환
num2 = float(input ('200 : ')) # str -> flcat (형변환)
result = num1 + num2 # 실수 = 정수 + 실수
print ('300.0 = ', 300.0)

# (1)  value 인수
print ('value =', 10 + 20 + 30 + 40 + 50)

# (2) sep 인수 : 값과 값을 특수문자로 구분
print('010', '1234', '5678', sep='-')

# (3) end 인수
print('value=', 10, end = ', ')

print('value=', 20)
