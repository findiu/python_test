import pickle
d={
    'name':'boy',
    'age':22
}
d['age']=23
#print(pickle.dumps(d))
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()