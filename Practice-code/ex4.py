print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
x=x+1
for i in range(x-1):
    for j in range(1,x):
        if i+j==x-1:
            print("*",end='')
        elif i+j>x-1:
            print("+",end='')   
        else :
            print(".",end='')
    for j in range(x-1):
        if i==j and i+j!=0:
            print("*",end='')
        elif i+j>i+i:
            print(".",end='')   
        elif i+j<i+i and j!=0:
            print("+",end='')    
        else :
            continue  
    for j in range(1,x):
        if j==1:
            # print("0",end='')
            continue
        elif i+j==x-1:
            print("*",end='')
        elif i+j>x-1:
            print("+",end='')   
        else :
            print(".",end='')
    for j in range(x-1):
        if i==j and i+j!=0:
            print("*",end='')
        elif i+j>i+i:
            print(".",end='')   
        elif i+j<i+i and j!=0:
            print("+",end='')    
        else :
            continue
    print("")
for i in range(2,(x*2)-2):
    for j in range((x*2)-2):
        if i==j:
            print("*",end='')
        elif i+j>i+i:
            print("+",end='')   
        elif i+j<i+i and j!=0:
            print(".",end='')    
    for j in range(2,(x*2)-2):
        if i+j==(x*2)-2:
            print("*",end='')  
        elif i+j<=(x*2)-2 :
            print("+",end='')
        else :
            print(".",end='')
    print("")

