class sum():
    def __init__(self,s):
        self.s=s
    
    def __str__(self):
        st=''
        for i in range(len(self.s)):
            st+=self.s[i]
        return st

a= sum('abcdefg')
print(a)
        