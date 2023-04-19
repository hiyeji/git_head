import random
guesses = 0
numMin = 1
numMax = 100
userInput = ''
randNum = random.randint(numMin, numMax)
print(numMin, "와(과)", numMax, '사이에 숫자를 입력하세요')

while True:
        userInput = int(input('숫자를 입력하세요'))
        guesses += 1
        if randNum == userInput :
            print('정답입니다')
            print('도전 횟수는?', guesses)
            break
        elif randNum > userInput :
            print('정답이 그보다 큽니다')
        elif randNum < userInput :
            print('정답이 그보다 작습니다')

num = int(input('점수 입력(1~100) : '))
print('num = ', num)

if num % 2 != 0 :
    print('홀수')
else :
    print('짝수')

#system 날짜/시간 모듈(*.py)
import datetime
