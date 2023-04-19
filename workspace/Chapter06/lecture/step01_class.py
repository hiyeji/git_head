# (1) 함수 정의
def calc_func(a,b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus() :
        m = x - y
        return m
    return plus, minus

# (2) 함수 호출
p, m = calc_func(10, 20)
print('plus =', p())
print('minus=', m())

# (3) 클래스 정의
class calc_class :
    x = y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

# (4) 객체 생성
obj1 = calc_class(10,20)

# (5) 멤버 호출
print('plus = ', obj1.plus()) # plus = 30
print('minus =', obj1.minus()) # minus = -10

class Car:
    # (1) 멤버변수
    cc = 0 # 엔진 cc
    door = 0 # 문짝 개수
    carType  = None # null

    # (2) 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType # 승용차, SUV

    # (3) 메서드
    def display(self):
        print('자동차는 %d cc이고, 문짝은 %d개, 타입은 %s'

              % (self.cc, self.door, self.carType))

# (4) 객체 생성
car1 = Car(2000, 4, '승용차') # 객체 생성 + 초기화
car2 = Car(3000, 5, 'SUV')

# (5) 멤버 호출 : object.member()
car1.display() # car1 멤버 호출
car2.display() # car2 멤버 호출
