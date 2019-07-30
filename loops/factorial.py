num=int(input("Enter no. you want factorial of :"))

fact=1

for i in range(num,0,-1):
    fact=fact*i

print("factorial of {} is {}".format(num, fact))
