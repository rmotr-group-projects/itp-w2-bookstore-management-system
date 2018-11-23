def create_bookstore(name):
    store = {}
    store['name'] = name
    store['books'] = []
    store['authors'] = []
    return store
    
def get_bookstore_name(bookstore):
    return bookstore['name']

def add_author(bookstore, name, nationality):
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author
    return None

def add_book(bookstore, title, isbn, author):
    book = {}
    book['title'] = title
    book['isbn'] = isbn
    book['author'] = author
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book
    return None


def get_books_by_author(bookstore, author):
    books_by_author = []
    for book in bookstore['books']:
        if book['author'] == author:
            books_by_author.append(book) 
    return books_by_author
