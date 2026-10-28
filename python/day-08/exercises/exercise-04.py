"""
Exercise 4 — Book dictionary
Create a dictionary for three books. Store each book's title, author, and year. Print every book and its details.
Challenge: search for a book by title.
"""

# Create a dictionary for three books
books = {
    "Book 1": {"author": "Author 1", "year": 2020},
    "Book 2": {"author": "Author 2", "year": 2019},
    "Book 3": {"author": "Author 3", "year": 2021}
}

# Print every book and its details
for title, details in books.items():
    print(f"Title: {title}")
    print(f"Author: {details['author']}")
    print(f"Year: {details['year']}")
    print()

# Challenge: search for a book by title
search_title = "Book 2"
if search_title in books:
    print(f"Found {search_title}:")
    print(f"Author: {books[search_title]['author']}")
    print(f"Year: {books[search_title]['year']}")
else:
    print(f"{search_title} not found.")