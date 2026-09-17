class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Bookshelf:
    def __init__(self):
        self.capacity = 6
        self.books = [None] * self.capacity
        self.current_count = 0

    def show_books(self):
        print("CURRENT BOOKSHELF")
        if self.current_count == 0:
            print("Bookshelf is empty.")
        else:
            for i in range(self.current_count):
                book = self.books[i]
                print(f"[{i}] Title: {book.title} | Author: {book.author} | Year: {book.year}")
        print("")

    def add_book(self, new_book):
        if self.current_count < self.capacity:
            self.books[self.current_count] = new_book
            self.current_count += 1
        else:
            print("\nERROR: Bookshelf is full. Cannot add more books.")

    def insertAt(self, new_book, position):
        if self.current_count == self.capacity:
            print("\nERROR: Bookshelf is full. Cannot add more books.")
            return

        if position < 0 or position > self.current_count:
            print("\nERROR: Invalid position. Cannot insert book.")
            return

        for i in range(self.current_count, position, -1):
            self.books[i] = self.books[i - 1]

        self.books[position] = new_book
        self.current_count += 1 

    def remove_At(self, position):
        if self.current_count == 0:
            print("\nERROR: Bookshelf is empty. Cannot remove any books.")
            return

        if position < 0 or position >= self.current_count:
            print("\nERROR: Invalid position. Cannot remove book.")
            return

        for i in range(position, self.current_count - 1):
            self.books[i] = self.books[i + 1]

        self.books[self.current_count - 1] = None
        self.current_count -= 1


my_bookshelf = Bookshelf()

MemoriaP = Book("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)
DomC = Book("Dom Casmurro", "Machado de Assis", 1899)
QuincB = Book("Quincas Borba", "Machado de Assis", 1891)

print("Welcome to the Bookshelf Program!")
print("Initializing with Machado de Assis classics...\n")

my_bookshelf.add_book(MemoriaP)
my_bookshelf.add_book(DomC)
my_bookshelf.add_book(QuincB)

while True:
    my_bookshelf.show_books()
    
    print("What would you like to do?")
    print("1. Add a book")
    print("2. Insert a book at a specific position")
    print("3. Remove a book from a specific position")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of publication: "))
        new_book = Book(title, author, year)
        my_bookshelf.add_book(new_book)
        
    elif choice == "2":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = int(input("Enter the year of publication: "))
        new_book = Book(title, author, year)
        position = int(input("Enter the position to insert the book: "))
        my_bookshelf.insertAt(new_book, position)
        
    elif choice == "3":
        position = int(input("Enter the position of the book to remove: "))
        my_bookshelf.remove_At(position)
        
    elif choice == "4":
        print("\nThank you for using the Bookshelf Program!")
        break
        
    else:
        print("\nERROR: Invalid choice. Please try again.")