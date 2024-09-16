# A pangram number is a number which contains at least once occurrence of each number.

#accepting the number as string
number=input("Enter the number :  ")

#creating a dictionary with all numbers as key and 0 as value
numCount={
    "1":0,
    "2":0,
    "3":0, 
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0,
}

#Incrementing the value in the dictionary if the key is present in the number
for i in number:
    if i in numCount:
        numCount[i]+=1

pangram=True
for i in numCount.values():
    if i == 0:
        pangram=False

if pangram:
    print("Entered number is a Pangram Number")
else:
    print("Entered number is not a Pangram")