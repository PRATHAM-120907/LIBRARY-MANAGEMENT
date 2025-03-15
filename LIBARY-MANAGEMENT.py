# list to store book as dictionaries

library = []

# fuction to add a book to the library

def add_book (title , aurthor , isbn):
    book = { 'title' :title , 'aurthor' : aurthor , 'isbn' : isbn , 'is_borrowed' : False}
    library.append(book)
    print(f"BOOK ADDED : {title}")


# function to display all the books 
def display_books():
    if not  library:
        print("NO BOOKS IN THE LIBARY")
    else:
        for book in library:
            status  = "BORROWED" if book['is_borrowed'] else "AVAILABLE"
        print(f"TITLE : {book['title']} , AURTHOR : {book['aurthor']} , ISBN : {book['isbn']} , STATUS : {status}")
            
# function to borrow a book 
def borrow_book (title):
    for book in library:
        if book['title'].lower() == title.lower():
            if not book['is_borrowed']:
                book['is_borrowed'] = True
                print(f"BOOK BORROWED : {book['title']}")
            else:
                print(f"BOOK ALREADY BORROWED : {book['title']}")
                return
            print(f"BOOK NOT FOUND :{title}")

# function to return a book 
def return_book (title):
    for book in library:
        if book['title'].lower() == title.lower():
            if book['is_borrowed']:
                book['is_borrowed'] = False
                print(f"BOOK RETURNED : {book['title']}")
            else:
                print(f"BOOK ALREADY RETURNED : {book['title']}")
                return
            print(f"BOOK NOT FOUND : {title}")


# main function for user interaction
def main ():
    while True:
        print("\n----LIBRARY MENU ----") 
        print("1) ADD BOOK ")
        print("2) DISPLAY BOOKS ")
        print("3) BORROW BOOK ")
        print("4) RETURN BOOK ")
        print("5) EXIT")

        choice =  input("ENTER YOUR CHOICE (1-5) : ")

        if choice == '1':
            title  = input("ENTER THE TITLE OF THE BOOK :")
            aurthor = input("ENTER THE AURTHOR OF THE BOOK :")
            isbn = input("ENTER THE ISBN OF THE BOOK :")
            add_book(title , aurthor , isbn)

        elif choice == '2':
            display_books()

        elif choice  =='3':
            title = input("ENTER THE TITLE OF THE BOOK TO BORROW :")
            borrow_book(title)

        elif choice  == '4':
            title = input("ENTER THE TITLE OF THE BOOK TO RETURN:")
            return_book(title)

        elif choice == '5':
            break

        else:
            print("INVALID CHOICE TRY AGAIN")

if __name__ =="__main__":
    main()

