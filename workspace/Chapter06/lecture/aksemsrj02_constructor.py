from statistics import mean
from math import sqrt

def Avg(data) :
    avg = mean(data)
    return avg

def var_sd(data) :
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data) -1 )
    sd = sqrt(var)

    return var, sd

data = [2, 4, 5, 6, 1, 8]
print('평균 = ', Avg(data))
var, sd = var_sd(data)
print('분산 =', var)
print('표준편차 =', sd)

from statistics import mean
from math import sqrt

def Avg(data) :
    avg = mean(data)
    return avg

def var_sd(data) :
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]

    var = sum(diff) / (len(data) -1)
    sd = sqrt(var)

    return var, sd

if __name__ == '__main__' :
    data = [1, 3, 5, 7]
    print('평균=' , Avg(data))
    var, sd = var_sd(data)
    print('분산=', var)
    print('표준편차=', sd)

print('사각형의 넓이를 계산합니다.')
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

print('사각형의 둘레를 계산합니다.')
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

