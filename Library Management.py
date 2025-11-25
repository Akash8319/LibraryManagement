class Library:
    def __init__(self):
        self.books = []
        self.status= {}

    def add_book(self, title):
        if title not in self.books:
            self.books.append(title)
            self.status[title] = "available"
            print("Book added!")
        else:
            print("Book aalready in Library.")

    def show_books(self):
        print("\nBooks in Library:")
        total_books = len(self.books)
        print(f"Totak Books: {total_books}")
        if not self.books:
            print("The library is empty.")
            return
        for i,book in enumerate(self.books):
            current_status = self.status.get(book,"unknown")
            print(f"{i+1}.{book} ({current_status.upper()})")

    def search_book(self, title):
        if title in self.books:
             current_status = self.status.get(title,"unknown")
             print(f"Book found! Status: {current_status.upper()}")
        else:
             print("Not found.")

    def remove_book(self, title):
        if title in self.books:
            if self.status.get(title) == "borrowed":
                print("Cannot remove: Bookk is currently borrowed.")
                return
            self.books.remove(title)
            del self.status[title]
            print("Book removed!")
        else:
            print("Book not found.")

    def borrow_book(self,title) :
        if title in self.books:
            if self.status.get(title) == 'available':
                self.status[title]= 'borrowed'
                print(f"'{title}' has been successfullyy borrowed.")
            else:
                print(f"'{title}' is already borrowed.") 
        else:
            print("Book not found in Library")           
        
    def return_book(self,title):
        if title in self.books:
            if self.status.get(title) == "borrowed":
                self.status[title]= "available"   
                print(f"'{title}' has been successfully returned.")
            elif self.status.get[title] == "avaiilable":
                print(f"'{title}' was not borrowed(it's already availble).")  
            else:
                print("'{title}' status is umknown.") 
        else:
            print("Book not found in library.") 



lib = Library()

while True:
    print("\n--- LIBRARY SYSTEM ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Borrow book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Book title: ")
        lib.add_book(title)

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        title = input("Search title: ")
        lib.search_book(title)

    elif choice == "4":
        title = input("Remove title: ")
        lib.remove_book(title)

    elif choice == "5":
        title = input(" Book Title to Borrow:") 
        lib.borrow_book(title) 

    elif choice == "6":
        title= input(" Book Title to Return:") 
        lib.return_book(title)     

    elif choice == "7":
        break

    else:
        print("Invalid choice!")