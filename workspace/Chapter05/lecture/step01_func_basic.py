# (1) builtins 함수
help(len)
dataset = list(range(1, 6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset)) # sum= 15
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics # (방법1)
from statistics import variance, stdev # (방법2)

print('평균=', statistics.mean(dataset)) # 방법1
print('중위수=', statistics.median(dataset)) # 방법1
print('표본 분산=', variance(dataset)) # 방법2
print('표본 표준편차=', stdev(dataset)) # 방법2

# (1) 인수가 없는 함수
def userFunc1() :
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1() # 함수 호출

# (2) 인수가 있는 함수
def userFunc2 (x, y) :
    print('userFunc2')
    z = x + y
    print('z=', z)

userFunc2(10, 20) # 함수 호출

# (3) return 있는 함수
def userFunc3(x, y) :
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

# 실인수 : 키보드 입력
x = int(input('x 입력 : '))
y = int(input('y 입력 : '))

t, s, n, d = userFunc3(x, y)
print('tot =', t)
print('sub =', s)
print('mul =', n)
print('div =', d)

from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

# (1) 산술평균
def Avg(data) :
    avg = mean(data)
    return avg

print('산술평균 =', Avg(dataset))

# (2) 분산/표준편차
def var_sd(data) :
    avg = Avg(data) # 함수 호출

    # list 내포
    diff = [ (d - avg)**2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

# (3) 함수 호출
v, s = var_sd(dataset)
print('분산 =', v)
print('표준편차=', s)
