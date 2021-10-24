x = map(int,input("enter -1:").split())
li=[]
count=[]

error =True
print(x)
for i in x:
    if i not in li:
        li.append(i)
        count.append(1)
    else :
        for j in range(len(li)):
            if i==li[j]:
                count[j]+=1

print(li)
print(count)
print(count.index(max(count)))
print(li[count.index(max(count))])

