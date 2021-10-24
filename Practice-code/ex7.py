num,y = map(int,input("Enter num and sub : ").split())
for i in range(y):
    if(num%10==0):
        num/=10
    else :
        num-=1
print(int(num))