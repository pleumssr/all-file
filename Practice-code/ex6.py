class translator:

    def deciToRoman(self, num):
        s=''
        while True: #num=900
            if num==0:
                break
            elif num/1000 >=1 :
                s+='M'
                num-=1000
            elif num/900 >=1:
                s+='CM'
                num-=900
            elif num/500 >=1:
                s+='D'
                num-=500
            elif num/400 >=1:
                s+='CD'
                num-=400
            elif num/100 >=1:
                s+='C'
                num-=100    
            elif num/90 >=1:
                s+='XC'
                num-=9
            elif num/50 >=1:
                s+='L'
                num-=50    
            elif num/40 >=1:
                s+='XL'
                num-=40
            elif num/10 >=1:
                s+='X'
                num-=10
            elif num/9 >=1:
                s+='IX'
                num-=9
            elif num/5 >=1:
                s+='V'
                num-=5
            elif num/4 >=1:
                s+='IV'
                num-=4
            elif num/1 >=1:
                s+='I'
                num-=1
        return s
    def romanToDeci(self, num):
        s=num
        # for i in range(len(num)):
        #     if i!=0:
        #         if num[i]== 'M':
        #             if num[i-1] in 'C':
        #                 continue
        #         if num[i]=='D':
        #             if num[i-1] in 'C':
        #                 continue
        #         if num[i]=='C':
        #             if num[i-1] in 'X':
        #                 continue
        #         if num[i]=='L':
        #             if num[i-1] in 'X':
        #                 continue
        #         if num[i]=='L':
        #             if num[i-1] in 'X':
        #                 continue
        #         if num[i]=='X':
        #             if num[i-1] in 'I':
        #                 continue
        #         if num[i]=='V':
        #             if num[i-1] in 'I':
        #                 continue
        #         if num[i] =='M':
        #             s+=1000
        #     elif num[i]=='C':
        #         if num[i]==num[-1]:
        #             if num[i+1]=='M':
        #                 s+=900
        #             elif num[i+1]=='D':
        #                 s+=400
        #             else :
        #                 s+=100
        #         else :
        #             s+=100
        #     elif num[i]=='D':
        #         s+=500
        #     elif num[i]=='X':
        #         if num[i]==num[-1]:
        #             if num[i+1]=='C':
        #                 s+=90
        #             elif num[i+1]=='L':
        #                 s+=40
        #         else :
        #             s+=40
        #     elif num[i]=='L':
        #         s+=50
        #     elif num[i]=='V':
        #         s+=5
        #     elif num[i]=='I':
        #         if num[i]==num[-1]:
        #             if num[i+1] == 'X':
        #                 s+=9
        #             elif num[i+1] == 'V':
        #                 s+=4
        #             else :
        #                 s+=1 
        #         else :
        #             s+=1 
        return s

    #     ### Enter Your Code Here ###
num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(num))


# print(translator().romanToDeci(translator().deciToRoman(num)))