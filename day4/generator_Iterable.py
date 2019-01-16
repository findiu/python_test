#列表生成式
#print([i*2 for i in range(10)])
#生成器:只有在调用时才会生成相应的数据，
#a1 = (i*2 for i in range(10000))
'''for i in a:
   print(i)
print(next(a))
aa=1
bb=2
aa,bb=bb,aa+bb
print(aa)
print(bb)'''
'''def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)'''
'''def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))
for i in fib(10):
    print(i)'''

def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i - 1] + N[i] for i in range(len(N))]
n = 0
for t in triangles():
     print(t)
     n = n + 1
     if n == 10:
        break

#可以直接作用for循环的对象都叫可迭代对象（如集合数据类型list,tuple,dict set str,和生成器，generator）
from collections import Iterable
print(isinstance([],Iterable))#判断是否为迭代对象

