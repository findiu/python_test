'''FamousDict = {
    '薛之谦':{
        '身高':178,
        '体重':130,
        '口头禅':['你神经病啊！','我不要面子啊']    #相应的值可以是 一个列表
    },
    '吴青峰':{
        '身高':170,
        '体重':120,
        '口头禅':['我叫吴青峰','你好']
    }
}
#print(FamousDict)
for i in FamousDict:
    print(i)'''
data={
    '广东':{
        '深圳':{
            '深汕区':['腾讯','云计算']
        },
        '广州':{
            '荔湾':['唯品会','电商']
        }
    },
    '广西':{
        '桂林':{
            '秀峰区':['随便','狗肉']
        },
        '玉林':{
            '王帝区':['厉害','山水']
        }
    }

}
for i1 in data:
    print(i1)
while True:
    chois1=input("1>>")
    if chois1 in data:
        for i2 in data[chois1]:
            print(i2)
        chois2=input("2>>")
        if chois2 in data[chois1]:
            for i3 in data[chois1][chois2]:
                print(i3)
            chois3=input("3>>")
            if chois3 in data[chois1][chois2]:
                for i4 in data[chois1][chois2][chois3]:
                    print(i4)
