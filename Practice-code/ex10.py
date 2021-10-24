class funString():
    def __init__(self,st = ""):
        ### Enter Your Code Here ###
        self.s=st
        self.strAns=''
    def __str__(self):
        return self.strAns
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.s)
        ### Enter Your Code Here ###

    def changeSize(self):
        for i in self.s:#self.s = [a,b,c,d]
            if ord(i)<97:
                x=ord(i)+32
                self.strAns+=chr(x)
            elif ord(i)>=97:
                x=ord(i)-32
                self.strAns+=chr(x)
        return self.strAns

        ### Enter Your Code Here ###

    def reverse(self):
        for i in range(len(self.s)-1,-1,-1):
            self.strAns+=self.s[i] #self.s'abcd'
        return self.strAns
        ### Enter Your Code Here ###

    def deleteSame(self):
        for i in self.s: #'aabbccdd'
            if i in self.strAns: #''
                continue
            else :
                self.strAns+=i
        return self.strAns #abcd
       ### Enter Your Code Here ###



str1,str2 = map(str,input("Enter String and Number of Function : ").split())
print(str1)
res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())

