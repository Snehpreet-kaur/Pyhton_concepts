#Creating Dictionary
info={"name" : "Snehpreet",
      "age" : 26 , 
      "city" : "Jamshedpur"
}

#accessing values in a dictionary
print (info["name"])
print (info)

#Creating list
List_info=["Snehpreet", 23, "Jamshedpur"]
print(List_info)
print(List_info[0])

#Get the list of keys from dictionary
print (info.keys())

#Fetch the list of values from dictionary
print (info.values())

#fetching the key and value of dictionary together
for key in info.keys():
    print(key, info[key])

#check if the key exists in the dicyionary or not
if "country" in info:
    print(info["country"])
else:
    print("Key doesnot exist")

#Add a key-value pair to the dictionary
info["Profession"]="Coding Instructor"
print (info)

#delete a key-value pair from the dictionary
del(info["Profession"])
print(info)

#changing a value in the dictionary
info["city"]="Ranchi"
print(info)

#Store a list as a value in the dictionary
info["marks"]=[90,92,80,70,60]
print(info)

#Access a value from the list stored in the dictionary
print(info["marks"][1])

#create a nested dictionary
classroom={"Snehpreet": {
    "age": 26,
    "marks":[90,80,95,70]
    },
    "Trisha": {
        "age":27,
        "marks": [80,70,86,92]
    }
}

#Go through basic dictionary operations for nested dictionary
print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
    print(i, classroom[i])

classroom["Trisha"]["age"]=28
print(classroom.values())



