import pickle
f=open('dump.txt','rb')
d=pickle.load(f)
print(d)
f.close()