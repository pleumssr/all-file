def check(lst,y):
    newlist = [1]
    for i in range(1,len(lst)):
        if(lst[y-i]==1+i):
            newlist.append(1+i)
            newlist.sort(reverse=True)
        else :
            break
    return newlist#newlist
print("*** Fun with countdown ***")
Mylist =list(map(int,input("Enter List : ").split(" ")))
result = [0,[]]
for i in range(len(Mylist)):
    if Mylist[i]==1:
        result[0]+=1
        result[1].append(check(Mylist,i))
print(result)