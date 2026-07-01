
#class method can access class variables and calles using cls

class Book:
    book_count = 0
    library_name = "City Library"

    #instance method
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.book_count += 1
    
    #class method
    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book1.change_library_name("Downtown Library")   