#Count the occurence of vowels in the string entered by the user

#Approach 1
sentence=input("Enter a string : ")
vowels = {"a": 0,
          "e": 0,
          "i": 0,
          "o": 0,
          "u": 0}

for i in sentence:
    if i in vowels:
        vowels[i] +=1

for i in vowels.keys():
    print(i,vowels[i])

#Approach 2
sentence=input("Enter a string : ")
vowelsList=['a','e','i','o','u']
vowels = {}

for i in sentence:
    if i in vowelsList:
        if i in vowels:
            vowels[i]+=1
        else:
            vowels[i] = 1

print (vowels)