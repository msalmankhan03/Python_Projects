import json
import pandas as pd
import matplotlib.pyplot as plt

class Library:
    def __init__(self, file_path='books.json'):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, isbn):
        for book in self.books:
            if book['isbn'] == isbn:
                print("ISBN already exists!")
                return
        book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def borrow_book(self, isbn):
        for book in self.books:
            if book['isbn'] == isbn:
                if book['available']:
                    book['available'] = False
                    self.save_books()
                    print(f"Book '{book['title']}' borrowed successfully!")
                else:
                    print(f"Book '{book['title']}' is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book['isbn'] == isbn:
                if not book['available']:
                    book['available'] = True
                    self.save_books()
                    print(f"Book '{book['title']}' returned successfully!")
                else:
                    print(f"Book '{book['title']}' is already available.")
                return
        print("Book not found.")

    def view_books(self, available_only=False):
        if not self.books:
            print("No books in the library.")
            return
        print("\nBooks in Library:")
        for book in self.books:
            if available_only and not book['available']:
                continue
            status = "Available" if book['available'] else "Borrowed"
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")

    def books_by_author(self):
        df = pd.DataFrame(self.books)
        if df.empty:
            print("No books to analyze.")
            return
        author_counts = df['author'].value_counts()
        plt.figure(figsize=(8, 5))
        author_counts.plot(kind='bar', color='skyblue')
        plt.title('Number of Books by Author')
        plt.xlabel('Author')
        plt.ylabel('Number of Books')
        plt.tight_layout()
        plt.savefig('books_by_author.png')
        plt.close()
        print("Bar chart saved as 'books_by_author.png'.")

def main():
    library = Library()
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. View Available Books")
        print("6. View Books by Author (Chart)")
        print("7. Exit")
        choice = input("Enter choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrow_book(isbn)

        elif choice == '3':
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == '4':
            library.view_books()

        elif choice == '5':
            library.view_books(available_only=True)

        elif choice == '6':
            library.books_by_author()

        elif choice == '7':
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()