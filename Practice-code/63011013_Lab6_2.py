def length(str) :
    if str == '':
        return 0
    else :
        return 1+length(str[1:])

def add(str,index):
    s=''
    if str=='':
        return s
    else:
        if index%2==0:
            s+=str[0]
            s+="*"
        else:
            s+=str[0]
            s+="~"
        return s+add(str[1:],index+1)

str = input('Enter Input : ')
print(add(str,0))
print(length(str))

 
