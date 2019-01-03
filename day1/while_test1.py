count=0
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
    if count==3:
        b=input("你想继续吗，SB？")
        if b!="n":
            count=0
#else:
    #print("你超过三次了")