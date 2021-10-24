h, w = map(float, input("Enter your High and Weight : ").split())
# h = float(input())
# w = float(input())
BMI = w/(h**2)
if BMI >= 30:
    print("Fat")
elif BMI >= 25:
    print("Getting Fat")
elif BMI >= 24:
    print("More than Normal Weight")
elif BMI >= 18.50:
    print("Normal Weight")
else :
    print("Less Weight")