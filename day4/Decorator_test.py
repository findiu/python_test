#装饰器，本质是函数（用来装饰其他函数）为其他函数添加附件功能
#不能改被装饰函数的函数内部
#不能改被装饰函数的调用方法

import time
'''def add(a,b):
    res=a+b
    print("a+b=",res)
f=add#函数就是 变量
f(2,4)
clac=lambda x:x*3#匿名函数
print(clac(3))

#嵌套函数
def foo():
    print("2")
    def dar():
        print("1")
    dar()
foo()'''

def log(func):
    def wrapp():
        print("wrapp")
        return func
    return wrapp
def now():
    print("now")
now=log(now)
now()


