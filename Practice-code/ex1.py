print("*** Rabbit & Turtle ***")
d, Vr,Vt,Vf = map(float, input("Enter Input : ").split())
print(d,Vr,Vt,Vf)
# print("Enter input :")
# d = int(input())
# Vr = int(input())
# Vt = int(input())
# Vf = int(input())
t=-d/(Vr-Vt)
s=Vf*t
print ("%.2f" % float(s))    