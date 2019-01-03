import getpass
name = "lwf"
pas = 123
username = input("usernaem:")
#passwd=getpass.getpass("passwd:")
passwd = int(input("passwd:"))
print(username,passwd)
if username == name and  passwd == pas:
    print("wlecome login")
else:
    print("name or pass corry")