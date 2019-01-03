#文件操作
'''f=open("gong1",'a',encoding='utf-8')#文件句柄 文件地址 a追加 ，W重写:直接创建文件。r读
f.write("曹尼玛11se\n")
f.write("傻吊")
f.close()
f=open("gong",'r',encoding='utf-8')
#for i in range(5):
#   print(f.readline())
#print(f.readlines())
for lins in f.readlines():
    print(lins.strip())
f.close()
f=open("gong",'r',encoding='utf-8')
for line in f:
    print(line.strip())#效率高
f.close()
f=open("gong",'r',encoding='utf-8')
print(f.readline())
print(f.tell())#打印句柄
f.seek(0)#回到句柄
print(f.tell())
print(f.readline())
print(f.encoding)
f.close()

f=open("gong1",'a',encoding='utf-8')
#f.write("sb\n")
#f.write("111111")
f.seek(10)
f.truncate(10)

f.close()

f=open('test','rb')
print(f.readline())
print(f.readline())
f=open('test','wb')
f.write('ff'.encode('utf-8'))
f.close()
f=open('gong','a+',encoding='utf-8')
print(f.readable())
print(f.writable())
f.write("\nheheh")
print(f.readline())
f.close()
print(f.closed)

f=open('gong','r+',encoding='utf-8')
print(f.readline())
f.write('sb')
f.close()

with open('gong','r+',encoding='utf-8') as f:
    print(f.readline())
    f.write('曹尼玛\n')

print(f.closed)'''













