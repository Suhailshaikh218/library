import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

# User details
USER_NAME = "MUHAMMAD SUHAIL SHAIKH"
USER_EMAIL = "mmuhammadsuhail234@gmail.com"

# Function to load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = json.load(file)  # Load JSON data
        return library
    return []

# Function to save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)  # Save JSON data with indentation

# Function to display user details
def display_user_details():
    print(f"\nWelcome, {USER_NAME}!")
    print(f"Email: {USER_EMAIL}\n")

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    favorite = input("Mark as favorite? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status,
        "favorite": favorite
    }
    library.append(book)
    print("Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Function to update a book
def update_book(library):
    title = input("Enter the title of the book to update: ")
    for book in library:
        if book["title"].lower() == title.lower():
            print("What do you want to update?")
            print("1. Title")
            print("2. Author")
            print("3. Publication Year")
            print("4. Genre")
            print("5. Read Status")
            print("6. Favorite Status")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                book["title"] = input("Enter new title: ")
            elif choice == "2":
                book["author"] = input("Enter new author: ")
            elif choice == "3":
                book["year"] = int(input("Enter new publication year: "))
            elif choice == "4":
                book["genre"] = input("Enter new genre: ")
            elif choice == "5":
                book["read"] = input("Have you read this book? (yes/no): ").lower() == "yes"
            elif choice == "6":
                book["favorite"] = input("Mark as favorite? (yes/no): ").lower() == "yes"
            else:
                print("Invalid choice!")
                return
            
            print("Book updated successfully!")
            return
    print("Book not found!")

# Function to search for a book
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        matching_books = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        matching_books = [book for book in library if author.lower() in book["author"].lower()]
    elif choice == "3":
        genre = input("Enter the genre: ")
        matching_books = [book for book in library if genre.lower() in book["genre"].lower()]
    else:
        print("Invalid choice!")
        return
    
    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, 1):
            status = "Read" if book["read"] else "Unread"
            favorite = "⭐" if book["favorite"] else ""
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status} {favorite}")
    else:
        print("No matching books found!")

# Function to display all books
def display_books(library):
    if not library:
        print("Your library is empty!")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        favorite = "⭐" if book["favorite"] else ""
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status} {favorite}")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    favorite_books = sum(1 for book in library if book["favorite"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")
    print(f"Favorite books: {favorite_books}")

# Function to sort books
def sort_books(library):
    print("Sort by:")
    print("1. Title")
    print("2. Author")
    print("3. Publication Year")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        library.sort(key=lambda x: x["title"].lower())
    elif choice == "2":
        library.sort(key=lambda x: x["author"].lower())
    elif choice == "3":
        library.sort(key=lambda x: x["year"])
    else:
        print("Invalid choice!")
        return
    
    print("Books sorted successfully!")
    display_books(library)

# Main function
def main():
    library = load_library()
    display_user_details()  # Display user details at the start
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Update a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Display statistics")
        print("7. Sort books")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            update_book(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            display_books(library)
        elif choice == "6":
            display_statistics(library)
        elif choice == "7":
            sort_books(library)
        elif choice == "8":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()