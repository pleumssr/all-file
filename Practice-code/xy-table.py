num = int(input("Enter : "))

for i in range(-num,num+1,+1):
    if i<0:
        x=-i
    else :x=i
    for j in range(-num,num+1,+1):
        if j<0:
            y=-j
        else :y=j
        if x>=y:
            # print(x,end='')
            if x%2==0:
                print("#",end='')
            else:print(" ",end='')
        else :
            # print(y,end='')
            if y%2==0:
                print("#",end='')
            else:print(" ",end='')
        # print(x,y,' ',end='')
    print('')
