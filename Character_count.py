#Count the occurence of each alphabet in the string entered by the user
sentence=input("Enter a string : ")
count ={}

for i in sentence:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i] = 1

for char in count.keys():
    print(char,"-", count[char])
#or you can just print(count)