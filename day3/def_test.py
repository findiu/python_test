'''def fun():
    "ddd"
    print('www')
    return 0
    print('heheheh')
x = fun()
print(x)
def fun1(x,y):
    print(x+y)
#fun1(10,22)
#fun1(y=10,x=10)
fun1(4,y=10)
def fun2(x,y,z=10):#形参z=10为默认参数
    print(x + y+z)
fun2(2,13,10)
fun2(2,3,z=10)
fun2(3,y=10,z=20)#关键字参数后面不能接位置参数
fun2(2,4)
def connet(hostname,port=3306):
    pass'''
def name(*args):#参数组，可以传入不定变量
    print(args,type(args))#接受n个关键字参数，转换为元组
name(1,2,3,4,5,6,7)
name(*[2,3,5,6])
def name1(**kwargs): #把n个关键字参数传人，转换为字典
    print(kwargs,type(kwargs))
name1(names='lwf',age=5,sex='n')
def set(name,t=10,*args,**kwargs):
    print(name)
    print(t)
    print(args)
    print(kwargs)
set('lwf',2,3,4,sex='f',age=10)



