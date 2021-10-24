li =[0,0,0,1,1,2,5]
print(li.count(0))
dic ={}
for i in li:
    try:
        dic[i]+=1
    except:
        dic[i]=0
print(dic)