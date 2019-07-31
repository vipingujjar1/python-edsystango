s=input("Enter string :")

print("In forward")

for i in range(len(s)):
    print(s[i])

print("In backward")

for i in range(len(s)-1,-1,-1):
    print(s[i])
