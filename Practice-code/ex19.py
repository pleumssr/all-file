x= [x for x in input("Enter Input : ").split(',')]
score=0
# print(x)
my = [i.split()[0] for i in x]
# print(my)
you =[i.split()[1] for i in x]
# print(you)

print("My   Queue = ",end='')
for i in my:
    if i != my[-1]:
        print(i,end=", ")
    else: print(i)

print("Your Queue = ",end='')
for i in you:
    if i != you[-1]:
        print(i,end=", ")
    else: print(i)
for i in range(len(my)):
    if my[i][0]==you[i][0] and my[i][2]==you[i][2]:
        score+=4
    elif my[i][0]==you[i][0] and my[i][2]!=you[i][2]:
        score+=1
    elif my[i][0]!=you[i][0] and my[i][2]==you[i][2]:
        score+=2
    else: score-=5
act=['Eat','Game','Learn','Movie']
pla=['Res.','ClassR.','SuperM.','Home']
# print(my)
# print(you)   
for i in range(len(my)):
    my[i]=list(my[i])
    you[i]=list(you[i])


for i in range(len(my)):
    my[i][0]=act[int(my[i][0])]
    my[i][2]=pla[int(my[i][2])]
    you[i][0]=act[int(you[i][0])]
    you[i][2]=pla[int(you[i][2])]
strmy=''
stryou=''
for i in range(len(my)):
    for j in range(len(my[0])):
        strmy+=my[i][j]
        stryou+=you[i][j]
    if i !=len(my)-1:
        strmy+=', '
        stryou+=', '
print("My   Activity:Location = "+strmy)
print("Your Activity:Location = "+stryou)    
if score >= 7:
    print("Yes! You're my love! : Score is "+str(score)+'.')
elif score >= 0:
    print("Umm.. It's complicated relationship! : Score is "+str(score)+'.')
else :print("No! We're just friends. : Score is "+str(score)+'.')