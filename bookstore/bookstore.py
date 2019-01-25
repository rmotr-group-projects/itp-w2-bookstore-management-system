# We are creating one store and chacking it a bunch of times
# using store in the tests.py
def create_bookstore(name):
    # You dont need to do return at the end.
    return {
        "name": name,
        # we dont need a key value pair so using a list
        "authors":[],
        "books":[]
    }


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
    }

    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        "title": title,
        "isbn": isbn,
        "author": author,
    }
    bookstore['books'].append(book)
    # If you dont have this everything will return None.
    return book
    
def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book

def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore['books']:
        if author == book['author']:
            books.append(book)
        
    return books
