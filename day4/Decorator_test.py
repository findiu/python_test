#装饰器，本质是函数（用来装饰其他函数）为其他函数添加附件功能
#不能改被装饰函数的函数内部
#不能改被装饰函数的调用方法
import time
def add(a,b):
    res=a+b
    print("a+b=",res)
f=add
f(2,4)
