class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass


class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self,base,bonus):
        self.pay = base + bonus
        print('총 수령액 : ', format(self.pay, '3, d'), '원)'

class Temporary(Employee) :
    def __init__(self, name):
        super().__init__(name)


def pay_calc(self, tpay, time):
    self.pay = tpay * time
    print('총 수령액 : ', format(self.pay, '3, d'), '원')

p = Permanent('홍길동')
p.pay_calc(2,500,000)


t = Temporary('김길동')
t.pay_calc(2, 400)

empType = input('고용형태 선택(정규직<P>, 임시직<T>) : ')
if empType == 'P ' or empType == 'p':

elif empType == 'T' or empType == 't':

else :
        print('=' * 30)
        print('입력 오류')