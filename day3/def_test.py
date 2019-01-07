def fun():
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
    pass
1111111111111