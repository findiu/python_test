f=open("gong",'r',encoding='utf-8')
f_new=open('gong.bak','w',encoding='utf-8')
for line in f:
    if '我年少轻狂' in line:
        line=line.replace('我年少轻狂','liweifan年少轻狂')
    f_new.write(line)
        #f_new.write('当liweifan年少轻狂')
    #else:
        #f_new.write(line)
f.close()
f_new.close()
