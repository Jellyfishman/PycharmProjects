def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('AAA',30))
print(person('BBB',35,city='北京'))
print(person('CCC',45,gender='M',job='Engineer'))
extra = {'city':'北京','job':'Engineer'}
print(person('DDD',24,city= extra['city'],job = extra['job']))