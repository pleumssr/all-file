x = [i for i in input("Enter Input : ").split('/')]
q=[]
# print(x)
before = x[0].split()
# print(before)
for i in before:
    q.append(i)
after = [i.split() for i in x[1].split(',')]
# print(after)
for i in after:
    if i[0]=='E':
        q.append(i[1])
    elif i[0]=='D':
        q.pop(0)
s=[]
check = True
for i in q:
    if i not in s:
        s.append(i)
    else:
        print("Duplicate")
        check=False
        break
if check==True:print('NO Duplicate')