num1=int(input("Enter value for num1 :"))
num2=int(input("Enter value for num2 :"))

even=odd=0

for i in range(num1,num2+1):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("No. of even no :", even)
print("No. of odd no :", odd)
