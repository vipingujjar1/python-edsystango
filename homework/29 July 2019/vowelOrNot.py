# check if word is vowel or consonent

word=str(input("Enter a word :")).lower()

if word=='a' or word=='e' or word=='i' or word=='o' or word=='u':
    print("{} is vowel.".format(word))
else:
    print("{} is consonent.".format(word))
