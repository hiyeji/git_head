def bank_account(bal) :
    balance = bal
    def getBalance() :
        return balance

    def deposit(money) :
        nonlocal balance
        balance += money

    def withdraw(money) :
        nonlocal balance
        balance -= money

    return getBalance, deposit, withdraw

bal1 = int(input('최초 계좌의 잔액을 입력하세요'))
getBalance, deposit, withdraw = bank_account(bal1)
print('현재 계좌 잔액은' + str(getBalance())+'원 입니다.')

bal2 = int(input('입금액을 입력하세요'))
print('입금후 잔액은' + str(deposit)+'원 입니다.')

bal3 = int(input('출금액을 입력하세요'))
print('출금후 잔액은' + str(withdraw)+'원 입니다.')
