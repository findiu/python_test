'''count=0
for i in range(3):
    i=10
    ii=int(input("请输入一个数字："))
    if i==ii:
        print("i=ii")
        break
    elif i > ii:
        print("i>ii")
    else:
        print("i<ii")
    count+=1
else:
    print("你超过三次了,死去吧")
for i in range(0,10):
    if i<5:
        print("loop",i)
    else:
        continue
    print("hehe...")'''
for n in range(10):
    print("----------",n)
    for m in range(10):
        print(m)
        if m>5:
            break

