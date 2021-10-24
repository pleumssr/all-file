def odd_even(arr,s):
    arrEven=[]
    arrOdd=[]
    sEven=''
    sOdd=''
    if type(arr)==list:
        if s=='Even':
            for i in range(len(arr)):
                if (i+1)%2==0:
                    arrEven.append(arr[i])
            print(arrEven)
        elif s=='Odd':
            for i in range(len(arr)):
                if (i+1)%2==1:
                    arrOdd.append(arr[i])
            print(arrOdd)
    if type(arr)==str:
        if s=='Even':
            for i in range(len(arr)):
                if (i+1)%2==0:
                    sEven+=arr[i]
            print(sEven)
        elif s=='Odd':
            for i in range(len(arr)):
                if (i+1)%2==1:
                    sOdd+=arr[i]
            print(sOdd)

# x='S'
# y='12345'
# z='Even'
print("*** Odd Even ***")
x,y,z=map(str,input("Enter Input : ").split(','))
if x =='L':
    y=y.split()
odd_even(y,z)
