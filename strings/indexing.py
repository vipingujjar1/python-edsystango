s=input("Enter a string :")
i=0
for x in s:
    print("+ve index {} and -ve index {} of char {}".format(i,i-len(s),x))
    i+=1
