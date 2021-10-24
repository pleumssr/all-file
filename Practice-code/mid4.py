print('*** String Rotation ***')
s=input("Enter 2 strings : ").split()
li1=list(s[0])
li2=list(s[1])
check =False
count =1
for i in range(2):
    temp=li1.pop(-1)
    li1.insert(0,temp)
for i in range(3):
    temp=li2.pop(0)
    li2.append(temp)

# print(count,*li1,*li2)
print(count,end=' ')
for i in li1:
    print(i,end='')
print(" ",end='')
for i in li2:
    print(i,end='')
print('')

while True:
    if li1==list(s[0]) and li2 ==list(s[1]):
        if count > 4:
            print(count,end=' ')
            for i in li1:
                print(i,end='')
            print(" ",end='')
            for i in li2:
                print(i,end='')
            print('')
        break
    for i in range(2):
        temp=li1.pop(-1)
        li1.insert(0,temp)
    for i in range(3):
        temp=li2.pop(0)
        li2.append(temp)
    count +=1
    if count <=5:
        print(count,end=' ')
        for i in li1:
            print(i,end='')
        print(" ",end='')
        for i in li2:
            print(i,end='')
        print('')
    else :
        if check==False:
            print(" . . . . .")
            check=True
print('Total of ',count,'rounds.')

