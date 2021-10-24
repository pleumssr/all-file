def sert_min(li,min,index):
    if index==len(li)-1:  #base case
        return min
        
    else:                 #recursinve case
        if li[index]<=min:
            min=li[index]
        return sert_min(li,min,index+1)
    

inp=list(map(int,input("Enter Input : ").split()))
min=sert_min(inp,inp[0],0)
print("Min :",min)