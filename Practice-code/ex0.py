# def romanToDeci(num):
#         s=0
#         for i in range(len(num)):
#             if num[i]== 'M':
#                 if num[i-1] in 'C':
#                     continue
#             if num[i]=='D':
#                 if num[i-1] in 'C':
#                     continue
#             if num[i]=='C':
#                 if num[i-1] in 'X':
#                     continue
#             if num[i]=='L':
#                 if num[i-1] in 'X':
#                     continue
#             if num[i]=='L':
#                 if num[i-1] in 'X':
#                     continue
#             if num[i]=='X':
#                 if num[i-1] in 'I':
#                     continue
#             if num[i]=='V':
#                 if num[i-1] in 'I':
#                     continue
#             if num[i] =='M':
#                 s+=1000
#             elif num[i]=='C':
#                 if num[i+1]=='M':
#                     s+=900
#                 elif num[i+1]=='D':
#                     s+=400
#                 else :
#                     s+=100
#             elif num[i]=='D':
#                 s+=500
#             elif num[i]=='X':
#                 if num[i+1]=='C':
#                     s+=90
#                 elif num[i+1]=='L':
#                     s+=40
#                 else :
#                     s+=10
#             elif num[i]=='L':
#                 s+=50
#             elif num[i]=='V':
#                 s+=5
#             elif num[i]=='I':
#                 if num[i+1] == 'X':
#                     s+=9
#                 elif num[i+1] == 'V':
#                     s+=4
#                 else :
#                     s+=1 
#         return s
# X='XXVV'
# print(romanToDeci(X))
# a='123456'
# a.remove(1)
# print(a[1])
# if ord('x') > ord('a') :
#     print(chr(ord('x')+1))
# s='IloveKMITL 3'
# # print(s[0])
# inp = [x.split() for x in input().split(',')]
# print(inp[0[0]])
# for i in range(10,-1,-1):
#     print(i)
# x='A'
# print(x)
# print(ord(x))
#x = [x for x in range(10)]
# x=[]
# for i in range(10):
#     x.append(i)
# print(x)
# x=[1,2,3,4,5,6]
# print(x)
# x='abcd'
# x=list(x)
# x[0]='0'
# print(x)

# s=''
# for i in range(len(x)):
#     s+=x[i]
# x=s

# print(x)
# for i in range(2,5,+1):
#     print(i)
# def sum(x):
#     x+=10
# x=0
# sum(x)
# print(x)
# x=[1,2,3,4]
# x.insert(3,6)
# print(x)
# li = map(int,input('enter : ').split())
# for i in li:
#     print(i+1)
# Python3 program to convert
# decimal number to roman numerals
 
ls=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
ls2=[]
 
# Function to convert decimal to Roman Numerals
def func(no,res):
    for i in range(0,len(ls)):
        if no in ls:
            res=dict[no]
            rem=0
            break
        if ls[i]<no:
            quo=no//ls[i]
            rem=no%ls[i]
            res=res+dict[ls[i]]*quo
            break
    ls2.append(res)
    if rem==0:
        pass
    else:
        func(rem,"")
 
 
# Driver code
if __name__ == "__main__":
    func(3549, "")
    print("".join(ls2))
 
# This code is contributed by
# VIKAS CHOUDHARY(vikaschoudhary344)