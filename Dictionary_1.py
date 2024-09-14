#create an empty dictionary
countrydata={}

#infinite loop
while True:
    #printing Menu
    print ("1. Insert \n2. Display all countries \n3.Display all capitals \n4. Get capital \n5. Delete")
    
    #get user's choice
    choice=int(input("Enter your choice(1-5)"))
    #condition to insert the country
    if choice == 1:
        country=input("Enter country: ").upper()
        capital=input("Enter capital: ").upper()
        countrydata[country]=capital
    
    #to display all countries
    elif choice == 2:
        print(list(countrydata.keys()))

    #to display all capitals
    elif choice == 3:
        print(list(countrydata.values()))

    #to display capital of specific country
    elif choice == 4:
        country=input("Enter country").upper()
        #printing the specific capital
        print(countrydata.get(country))

    #to delete entry of a specific country
    elif choice == 5:
        country=input("Enter country: ").upper()
        del countrydata[country]

    #if none of the above options
    else:
        print("Invalid Input")
        break