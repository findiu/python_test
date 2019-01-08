'''def name(age):
    print(age)
age=10
name(20)
print(age)'''
s=10
def name(age):
    global s  #定义global变量不能是参数，尽量不要用
    s=20#局部变量
    age=20
    print('age=',age)
    print('s=',s)
age = 10
name(20)
print('age=',age)
print('s=',s)
names=['lwf','age','job'] #在函数中列表可以改变全局变量
def chang_name():
    names[0]='wj'
    print(names[0])
chang_name()
print(names[0])
