# A very basic python program in python for new learners
print("Welcome to eazy book store\n")
#this is a book store where you can buy your book
#fuctions initialized
def add():
    print("Welcome please let us know about your book\n")
    know = input("what is your book type\n1.Love\n2.Action\n:/")
    book = input("\ngreat now tell us the name of your book: ")
    print("\nyour book was added successfully\nhave a great day :)")
#books are out of stock will be availble to buy on my book store website
def books(type):
    action_books = ["robos action","robos fight"]
    love_books = ["robos love","robos secret"]
    if(type == "1" or type == "LOVE"):
        print("the books are" ,love_books, "\nbooks are currently out of stock but will be avilable soon")
    elif(type == "2" or type == "ACTION"):
        print("the books are", action_books ,"\nbooks are currently out of stock but will be avilable soon")
    else:
        print("the available books are", action_books,love_books , "books are out of stock but will be avilable soon")

def buy():
    print("glad to see you here you can buy any one of the book provided here")
    type = input("you can specify a type too\n1.ACTION\n2.LOVE\n:/")
    books(type)
    


#main code (I was a cpp devloper)
print("the only bookstore which allows you to add your own book sell")
print("\n\n")
operation = input("what do need\n1.add book(ADD)\n2.buy a book(BUY)\n:/ ")
if(operation == "1" or operation == "ADD"): 
#taking 1 as int as not defined but you can define using int operation/function
    add()
elif(operation == "2" or operation == "BUY"):
    buy()
else:
    print("not valid")
    
    
    