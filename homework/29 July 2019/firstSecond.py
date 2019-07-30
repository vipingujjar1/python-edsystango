#check if a no. is compleatly divisible or not

num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))

if num1%num2==0:
    print("{} is divisible by {}.".format(num1, num2))
else:
    print("{} is not divisible by {}".format(num1, num2))
