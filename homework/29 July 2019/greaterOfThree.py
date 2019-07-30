# check which one is greater out of three

num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
num3=int(input("Enter num3 :"))

if num1>num2 and num1>num3:
    print("{} is greater than {} and {}".format(num1,num2,num3))
elif num2>num1 and num2>num3:
    print("{} is greater than {} and {}".format(num2,num1,num3))
elif num3>num1 and num3>num2:
    print("{} is greater than {} and {}".format(num3,num1,num2))
else:
    print("All are equal")
