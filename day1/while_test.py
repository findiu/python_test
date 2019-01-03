'''count=0
while count<3:
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
    print("你超过三次了")
i=0
while True:
    print("i:",i)
    #i=i+1
    i+=1
    if i==1000:
        break'''
for i in range(0,10,3):
    print("loop:",i)

