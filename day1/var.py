#！/usr/bin/env python
#linux必须写
#-*- conding:utf-8 -*-
#python2必须写
'''print(name)
name=1
'''
#注析
#打印多行字符串
#单双引号没区别
msg='''print(name)
name=1
'''
print(msg)
name="lwf"
name2=name
print(name,name2)
name="qqqqq"
print(name,name2)
st="你好，手机"
print(st)
'''username=input("username:")
passwd=input("passwd:")
print(username,passwd)'''
#任何数字输入是字符串
#不要用拼接，效率低
name=input("name:")
age=int(input("age:"))
s='''----info of %s-----
         name:%s
         age:%d
   --------------------
'''%(name,name,age)
print(s)
print(type(age),type(str(age)))

s2='''----info of {_name}-----
         name:{_name}
         age:{_age}
   --------------------
'''.format(_name=name,_age=age)
print(s2)





