import json
d={
    'name': 'lwf',
    'age': 22
}
#print(json.dumps(d))
f=open('json1.txt','w',encoding='utf-8')
json.dump(d, f)
f.close()