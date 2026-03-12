class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
book1 = Book("Python Basics", "Alice Smith", "1234567890", 2020)
book2 = Book("Advanced Python", "Bob Johnson", "0987654321", 2018)

print(book1.get_summary())
print(f"Age of book1: {book1.get_age()} years")

print(book2.get_summary())
print(f"Age of book2: {book2.get_age()} years")