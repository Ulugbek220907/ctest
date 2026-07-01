#magic methods = dunder methods 


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return len(self.title)

    def __add__(self, other):
        if isinstance(other, Book):
            return f"{self.title} and {other.title}"
        return NotImplemented

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(book1)  # Uses __str__
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(len(book1))  # Uses __len__
print(book1 + book2)  # Uses __add__
print(str(book1))