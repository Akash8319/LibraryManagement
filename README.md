# library_management
class Library:
    """
    A class used to represent a Library Management System.

    Attributes
    ----------
    books : list
        A list used to store the names of the books in the library.
    status : dict
        A dictionary mapping book titles to their current status (e.g., 'available', 'borrowed').
    """

    def __init__(self):
        """Initializes the Library with empty storage structures."""
        self.books = []
        self.status = {}

    def add_book(self, title):
        """
        Adds a new book to the library inventory.

        Parameters
        ----------
        title : str
            The title of the book to add.
        """
        if title not in self.books:
            self.books.append(title)
            self.status[title] = "available"
            print(f"Success: '{title}' added to library.")
        else:
            print(f"Error: '{title}' already exists in the library.")

    def show_books(self):
        """Displays all books currently in the inventory with their status."""
        print("\n--- Current Inventory ---")
        if not self.books:
            print("The library is currently empty.")
            return
        
        print(f"Total Assets: {len(self.books)}")
        for i, book in enumerate(self.books):
            current_status = self.status.get(book, "unknown")
            print(f"{i + 1}. {book} [{current_status.upper()}]")

    def search_book(self, title):
        """
        Searches for a specific book and prints its status.

        Parameters
        ----------
        title : str
            The title of the book to search for.
        """
        if title in self.books:
            current_status = self.status.get(title, "unknown")
            print(f"Result: '{title}' found. Status: {current_status.upper()}")
        else:
            print(f"Result: '{title}' not found in inventory.")

    def remove_book(self, title):
        """
        Removes a book from the library if it is not currently borrowed.

        Parameters
        ----------
        title : str
            The title of the book to remove.
        """
        if title in self.books:
            if self.status.get(title) == "borrowed":
                print(f"Action Denied: '{title}' is currently borrowed and cannot be removed.")
                return
            self.books.remove(title)
            del self.status[title]
            print(f"Success: '{title}' removed from library.")
        else:
            print("Error: Book not found.")

    def borrow_book(self, title):
        """
        Updates a book's status to 'borrowed' if it is available.

        Parameters
        ----------
        title : str
            The title of the book to borrow.
        """
        if title in self.books:
            if self.status.get(title) == 'available':
                self.status[title] = 'borrowed'
                print(f"Success: You have borrowed '{title}'.")
            else:
                print(f"Unavailable: '{title}' is already borrowed.")
        else:
            print("Error: Book not found in Library.")

    def return_book(self, title):
        """
        Updates a book's status to 'available' if it was borrowed.

        Parameters
        ----------
        title : str
            The title of the book to return.
        """
        if title in self.books:
            if self.status.get(title) == "borrowed":
                self.status[title] = "available"
                print(f"Success: '{title}' returned successfully.")
            elif self.status.get(title) == "available":
                print(f"Notice: '{title}' was not borrowed (already available).")
            else:
                print("Error: Status unknown.")
        else:
            print("Error: Book not found in library.")
