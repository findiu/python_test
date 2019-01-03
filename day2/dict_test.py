#dict key-value
info={
    'name1':'liweifan',
    'job':'it',
    'year':'100',
    'name2':'lwf'
}
#print(info)


'''
info['job']='kf'
info['wife']='siting'
#del info['name2']
info.pop('name2')
#print(info['job'])
print(info.get('name'))
print('name2' in info)'''
b={
    'stu1':'liwei',
    'stu2':'wengjie',
    'name2': 'lwf1'
}
#info.update(b)

#print(info)
#print(info.items())
#c=dict.fromkeys([3,5,6],'hehe')
#print(c)
#print(info)

for i in info:
    print(i,info[i])
for k,v in info.items():#高效
    print(k,v)

