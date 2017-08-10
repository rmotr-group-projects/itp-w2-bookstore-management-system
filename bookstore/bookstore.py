def create_bookstore(name):
    store = {}
    store['name'] = name
    store['author_id'] = 0
    store['author'] = []
    store['books'] = []
    store['book_id'] = 0
    return store

def add_author(bookstore, name, nationality):
    bookstore['author_id']  =  bookstore['author_id']+ 1
    author = {
        'name': name,
        'nationality' : nationality,
        'id' : bookstore['author_id'] 
        }
    bookstore['author'].append(author)
    return author
    

def get_author_by_name(bookstore, name):
    for author in bookstore['author']:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['author']:
        if author['id'] == author_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    bookstore['book_id'] = bookstore['book_id'] + 1
    book = {
        'title' : title,
        'isbn': isbn,
        'id': bookstore['book_id'],
        'author_id' : author_id
        }
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    book_authors = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            book_authors.append(book)
    return book_authors
