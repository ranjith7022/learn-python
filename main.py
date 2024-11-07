class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_books(self, search_string):
        list1 = []
        for i in self.books:
            if search_string in i.title.lower() or search_string in i.author.lower():
                
                list1.append(i)
        return list1
        
