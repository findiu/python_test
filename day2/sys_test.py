#标准库在lib 第三方库在site-packers
'''import sys
print(sys.path)#打印环境变量
print(sys.argv)#打印脚本名字路径pwd
#print(sys.argv[2])
import  os
#dir_name=os.system("dir")#只执行结果，不保存结果
dir_name=os.popen("dir").read()
print("----",dir_name)
#os.mkdir("day3")
#import day1.var'''
#数据类型  bool False只为0
print(bool(0))
print(bool(-2))
#三元运算
a,b,c=1,2,5
a=b if a>b else c
print(a)
#bytes和字符串的转换，在网络编程中是以字节进行传输的
msg="我是大帅哥"
print(msg.encode(encoding="utf-8"))
a=b'\xe6\x88\x91\xe6\x98\xaf\xe5\xa4\xa7\xe5\xb8\x85\xe5\x93\xa5'.decode(encoding="utf-8")
print(a)
