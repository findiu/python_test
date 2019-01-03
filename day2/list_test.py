#列表list
import copy
name=["1lwf","!wj","jiaob","Hwj",["李小乐","王杰"],"!wj"]#多沉列表是指针 ，cope只拷贝指针
#name.append("lf")
#name.insert(3,"xiaopeng")
#name[0]="hehe"
#name.remove("wj")
#del name[1]
#name.pop()
#name.pop(0)
#print(name)
#print(name.index("wj"))
#print(name.count("wj"))
#name.clear()
#name.reverse()
#name.sort()
#name1=[1,2,3,4]
#name.extend(name1)
#name2=name.copy()#浅copy列表内的列表只copy指针，列表copy了一份
#name2=name#指针指向了列表
'''name2=copy.deepcopy(name)#深copy
name[0]="傻逼"
name[4][0]="丝毫"
print(name)
print(name2)'''
for i in name:#循环
    print(i)
#print(name[::2])#列表切片


'''print(name[0])
print(name[0:2])   #切片
print(name[-1])
print(name[-2:-1])
print(name[-2:])
print(name[:3])'''

