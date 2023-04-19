from re import findall
from statistics import mean

emp = ['2014홍길동220', '2002이순신300', '2010유관순260']

def pay_pro(emp) :

emp_re1 = [sub('[0-9]','', emp) for emp in emp]
print('emp_re1 :', emp_re1)

emp_re2 = [sub('[,.?!:;]', '', emp_re1)]
print('emp_re2 :', emp_re2)

emp_re3 = [' '.join(emp.split() for emp in emp_re2)]
print('emp_re3 :', emp_re3)

pays_mean = pay_pro()
print('전체 사원의 급여 평균 :', pays_mean)

from re import findall
from statistics import mean

emp = ['2014홍길동220', '2002이순신300', '2010유관순260']

def pay_pro(x):
    from statistics import mean
    import re

    emp_re1 = sub('[0-9]', '', emp_re)
    emp_re2 = sub('[,.?!:;]', '', emp_re1)
    emp_re3 = ' '.join(emp_re3.split())
    return emp_re3

pay_pro(emp)
emp_result = [clean_emp(emp) for emp in emp]
print(texts_result)

