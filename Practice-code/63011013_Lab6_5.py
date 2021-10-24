def staircase(num,inp):
    if num==0:
        return
    else :
        if num<0:
            loop2(num*-1,inp*-1)#num=3,2,1
            staircase(num+1,inp)
        else:
            loop(num,1,inp)#num=3,2,1
            staircase(num-1,inp)

def loop(num,count,len):
    if len==0:
        print('')
        return
    else :
        if count>=num:
            print('#',end='')
        else :
            print('_',end='')
        loop(num,count+1,len-1)

def loop2(num,len):
    if len==0:
        print('')
        return
    else :
        if len<=num:
            print('#',end='')
        else :
            print('_',end='')
        loop2(num,len-1)
        
inp=int(input("Enter Input : "))
if inp==0:
    print("Not Draw!")
else:
    staircase(inp,inp)