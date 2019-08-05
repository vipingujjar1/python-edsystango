
a=[]

even=[]
odd=[]

for i in range(1,51):
    a.append(i)

for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
