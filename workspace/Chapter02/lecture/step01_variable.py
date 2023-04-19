# 1. 변수, 메모리 주소,
from Chapter02.lecture.step02_std_input_output import result

var1 = 'Hello python'
print(var1)
print( id(var1) )

var2 = 100
print(var2)
print( id(var2) )

var2 = 150.25
print(var2)
print( id(var2) )
print(type(var2))

var3 = True
print(var3)
print( id(var3) )
print(type(var3))

# 2. 예약어 확인

print(python_keyword)


print (type(python_keyword))_# <class 'list'>
print(len(python_keyword))_# 35


#3. 자료링 변환(Casting)

# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a+b
print('add = ', add)

# 정수 _> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

# 논리형 -> 정수
print ( int(True) ) # 1
print ( int(False) ) # 0

# 문자형 -> 정수
st = '10'
print( int (st) ** 2 ) # 제곱 연산

num1 = 100 # 피연산자1
num2 = 20 # 피연산자2

add = num1 + num2 # 덧셈
print ('add=', add)
sub = num1 - num2 # 뺄셈
print (sub)
nu1 = num2 * num2 # 곱셈
print (nu1)
div = num1 / num2 # 나눗셈
print (div)
div2 = num1 # num2 # 나머지 계산
print (div2)
square = num2**2 # 제곱 계산
print (square)

# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print (bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print (bool_result)

# (2) 크기비교
bool_result = num1 > num2 #num2값이 큰지 비교
print (bool_result)
var = bool_result + num1 >= num2  # num1값이 크거나 같은지 비교
print (bool_result)
bool_result = num1 < num2 # num2 값이 큰지 비교
print (bool_result)
bool_result = num1 <= num2 # num2 값이 크거나 같은지 비교
print (bool_result)

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <=10
print(log_result)

# 3. 논리 연산자 예문
log_result = num1 >= 50 and num2 <=10 # 두 관계식이 같은지 판단
print(log-result)_# FALSE
log_result = num1 >= 50 or num2 <=10 # 두 관계식 중 하나라도 같은지 판단
 print(log_result)

log_result + num1 >= 50_# 관계식 판단
print(log_result)
log_result+not (num1 >= 50# 괄호 안의 관계식 판단 결과에 대한 부정
print (log_result)

# 4. 할당 연산자
# 1) 변수의 값 할당(=)
i = tot = 10 # i=10; tot = 10
i += 1 # i = i + 1
tot += i # tot = tot + 1
print(i, tot)

# 같은 줄에 중복 출력
print ('출력1', end=' , ') # end= '구분자'
print('출력2')

v1, v2 = 100,200
# (2) 변수 교체
v2, v2 = v2, v2
print (v2, v2) # 200 100

# (3) 패킹(packing) 할당
lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print (v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = 1st
print (v1, v2) # [1, 2, 3, 4] 5

