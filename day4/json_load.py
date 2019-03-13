import json
f=open('json1.txt','r',encoding='utf-8')
d=json.load(f)
print(d,type(d))
f.close()
d1='{"name":"lwf","age":22}'
print(type(d1))
d2=json.loads(d1)
print(d2,type(d2))