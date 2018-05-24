# -*- coding: utf-8 -*-
n = 0

a = input('身高(cm):')
b = input('体重(Kg):')
height = float(a)/100
weight = float(b)
bmi = weight/(height**2)
print('BMI',bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25 and bmi >= 18.5:
    print('正常')
elif bmi < 28 and bmi >= 25:
    print('过重')
elif bmi < 32 and bmi >= 28:
    print('肥胖')
else:
    print('严重肥胖')