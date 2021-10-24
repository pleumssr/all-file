
print(" *** Recite the multiplication table ***")
cir = [x.split() for x in input("Enter pattern for child 1 to 3 (-1 for sep) : ").split('-1')]
print('')
print('Pattern for child 1 :',*cir[0])#[1 2 3]
print('Pattern for child 2 :',*cir[1])#[2 3 4 5]
print('Pattern for child 3 :',*cir[2])#[9 8 7 6 5 4]

i=0
j=0
k=0
count=1
while True:
    if count > len(cir[0])*len(cir[1])*len(cir[2]):
        print("This year they never recite same multiplication table !!!")
        break
    if cir[0][i]==cir[1][j] and cir[0][i]==cir[2][k]:
        # print("final")
        print("They recite same multiplication table in",count,'days')
        break
    if i+1>len(cir[0])-1:
        i=0
    else:i+=1

    if j+1>len(cir[1])-1:
        j=0
    else:j+=1

    if k+1>len(cir[2])-1:
        k=0
    else:k+=1

    count+=1



