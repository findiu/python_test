import random
print("猜数字")
i=random.randint(0,100)
print(i)
ii=int(input("请输入一个数字(0~100)："))
while i!=ii:
    if i > ii:
        print("你输入得数字小了")
        ii = int(input("请重新输入一个数字(0~100)："))
    elif i<ii:
        print("你输入得数字大了")
        ii = int(input("请重新输入一个数字(0~100)："))
print("恭喜你，答对了")