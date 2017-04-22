import os
def files():
    dic={}
    for root, dirs, files in os.walk('.'):
        for f in files:
            f = f[f.rfind('.')+1:]
            if f not in dic:
                dic[f] = 1
            else:
                dic[f]+=1
    for key in dic:
        if dic[key] == max(dic.values()):
            return key
print(files())
                
