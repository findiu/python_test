import pymysql
db = pymysql.connect("172.18.100.39", "root", "toor", "pescms")
cursor = db.cursor()
#cursor.execute('create database pythondb;')
cursor.execute('use pescms;')
print(cursor.execute('show tables;'))
cursor.close()#先关闭游标
db.close()#再关闭数据库连接
#print('创建pythonBD数据库成功')
