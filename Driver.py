from textbook import Book
print("Please enter the requiered information for the 1st book.")


def book_description():
    title = str(input("Title: "))
    first = str(input("First name:"))
    last = str(input("Last name:"))
    age = str(input("Age: "))
    edition = str(input("Edition: "))
    ISBN_number = str(input("ISBN number: "))
    publisher = str(input("Publisher: "))
    year_published = str(input("Year published: "))
    quantity = str(input("Number of books: "))
    price = str(input("Price: "))
    book = Book(title,first, last, age,edition,ISBN_number,publisher,year_published,quantity,price)
    return book


book1 = book_description()
book2 = book_description()
menu_choice = 0
while  menu_choice != 4:
    print("What would you like to do, please select from the menu below.")
    print("1. add to inventory.")
    print("2. deduct from inventory.")
    print("3. Modify the price of a book.")
    print("4. Quit the programm")

    menu_choice = int(input())

    if menu_choice == 1:
        print(f"Which book, '{book1.title}' or '{book2.title}'")
        choice = int(input())
        if choice == book1.title:
            qty = int(input("How much would you like to add?"))
            book1.add_quantity(qty)
            print("The quantity in inventory is now " + str(book1.quantity + "\n\n"))
        elif choice == book2.title:
            qty = int(input("How much would you like to add?"))
            book2.add_quantity(qty)
            print("The quantity in inventory is now " + str(book2.quantity + "\n\n"))
        else:
            print("Error, please enter the correct title.")
    elif menu_choice == 2:
        print(f"Which book, '{book1.title}' or '{book2.title}'")
        choice = int(input())
        if choice == book1.title:
            qty = int(input("How much would you like to remove?"))
            result = book1.deduct_quantity(qty)
            if result == 0:
                print("The quantity in inventory is now 1" + str(book1.quantity) + "\n\n")
            else:
                print("You do not have enough books in inventory to remove that quantity")
                print("Curretn inventory in stock is" + str(book1.quantity) + "\n\n")

        elif choice == book2.title:
            qty = int(input("How much would you like to remove?"))
            result = book2.deduct_quantity(qty)
            if result == 0:
                print("The quantity in inventory is now 1" + str(book2.quantity) + "\n\n")
            else:
                print("You do not have enough books in inventory to remove that quantity")
                print("Current inventory in stock is" + str(book2.quantity) + "\n\n")
        else:
            print("Error, please enter the correct title.")

    elif menu_choice == 3:

        print(f"Which book, '{book1.title}' or '{book2.title}'")
        choice = int(input())
        if choice == book1.title:
            price = float(input("What will the new price be: "))
            book1.price = price
            print(f"The price of {book1.title} is now {book1.price}")
        elif choice == book2.title:
            price = float(input("What will the new price be: "))
            book2.price = price
            print(f"The price of {book2.title} is now {book2.price}")
        else:
            print("Error, please enter the correct title.")

    elif menu_choice == 4:
        print("Thank you for using the system!")
    else:
        print("Error, please enter a number on the menu.")
