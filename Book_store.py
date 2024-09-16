#creating a dictionary of textbooks and its cost
books={
    "Maths":650,
    "English":400,
    "Physics":140,
    "Chemistry":280,
    "Biology":360,
    "Computer":420
}
#rectifying the price of Physics
books["Physics"]=200

#Adding the cost of 2 more books to dictionary
books["History"]=300
books["Geography"]=250

#printing the cost of the book entered by the user
book=input("Enter the book whose price you want to know.. ")
for i in books.keys():
    if i==book:
        t=(books[book])
        break
    else:
        t="Invalid Input"
print("Rs ",t)

#printing all the books and their cost
for book in books.keys():
    print(book,"= Rs", books[book])