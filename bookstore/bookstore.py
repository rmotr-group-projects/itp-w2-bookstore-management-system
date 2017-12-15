def create_bookstore(name):
    bookstore = {
        'store': name,
        'authors': {},
        'books': []
    }
    #import pdb; pdb.set_trace()
    return bookstore


def get_bookstore_name(bookstore):
    return bookstore['store']

def add_author(bookstore, name, nationality):
    bookstore['authors'][name] = {
        'name': name,
        'nationality': nationality
    }
    return bookstore['authors'][name]


def get_author_by_name(bookstore, name):
    return bookstore['authors'][name]


def add_book(bookstore, title, isbn, author):
    book = {
        'title': title,
        'isbn': isbn,
        'author': author
    }
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_books_by_author(bookstore, author):
    books_by_author = []
    for book in bookstore['books']:
        if book['author'] == author:
            books_by_author.append(book)
    return books_by_author
      
