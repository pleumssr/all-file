a = []
a = input("Enter number end with (-1) : ").split()
error = True
error2 = False
U = []
U2 = []
A = 0
B = ''
for i in a:
    if i in a:
        if i == "-1":
            if a[0] == "-1":
                error2 = True
                error = False
            else:
                error = False
            break
        else:
            U.append(i)
for i in U:
    if i not in U2:
        U2.append(i)
for i in U2:
    # U = 0 0 0 1 2 5
    # U2 = 0 1 2 5
    num = U.count(i)
    if num == A:
        error2 = True
    elif num > A:
        error2 = False
        A = num
        B = i

if error == True:
    print('Invalid INPUT !!!')
elif error2 == True:
    print('Not found')
else:
    print(B)