def hbd(age):
    s=''
    if age%2!=0:
        age-=1
        s='saimai is just 21, in base '+str(int(age/2))+'!'
    elif age%2!=1:
        s='saimai is just 20, in base '+str(int(age/2))+'!'
    return s

year = input("Enter year : ")

print(hbd(int(year)))