# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
x = input('汉诺塔层数:')
y = int(x)

print(move(y,'A','B','C'))
