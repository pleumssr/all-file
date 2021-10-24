class py_solution:
    def __init__(self,num):
        self.num=num
        self.val=num
    def int_to_Roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = {
             1:"M", 2:"CM", 3:"D", 4:"CD",
            5:"C", 6:"XC", 7:"L", 8:"XL",
            9:"X", 10:"IX", 11:"V", 12:"IV",
            13:"I"
        }
        roman_num = ''
        i = 0
        while  self.num > 0:
            while self.num//val[i]>0:
                roman_num += syb[i+1]
                self.num -= val[i]
            for _ in range(self.num // val[i]):
                roman_num += syb[i]
                self.num -= val[i]
            i += 1
        return roman_num
    def __add__(self, other):
        print(self.num+other)
        return py_solution(self.num + other)
    def add(self,other):
        sum=self.val+other
        sum2=sum/2
        print(self.val,'+',other,'=',end=' ')
        print(int(sum+sum2))

print(" *** class MyInt ***")
x = input("Enter 2 number : ").split()
a=py_solution(int(x[0]))
b=py_solution(int(x[1]))
print(x[0],"convert to Roman :",a.int_to_Roman())
print(x[1],"convert to Roman :",b.int_to_Roman())
a.add(b.val)
