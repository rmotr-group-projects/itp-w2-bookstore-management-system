def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors':{},
        'book': {},
    }
    return bookstore


def add_author(bookstore, name, nationality):
    authors = {
        'name': name,
        'nationality': nationality,
        'id': name,
    }
    bookstore['authors'][name] = authors
    return authors


def get_author_by_name(bookstore, name):
    return bookstore['authors'][name]


def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]


def add_book(bookstore, title, isbn, author_id):
    books = {
        'title': title,
        'isbn': isbn,
        'author_id': author_id,
        'id': title,
    }
    bookstore['book'][title] = books
    return books


def get_book_by_title(bookstore, title):
    return bookstore['book'][title]


def get_book_by_id(bookstore, book_id):
    for key in bookstore['book']:
        get_book = bookstore['book'][key]
        if book_id == get_book['id']:
            return get_book


def get_books_by_author(bookstore, author_id):
    books = []
    for key in bookstore['book']:
        book_by_author = bookstore['book'][key]['author_id']
        if author_id == book_by_author:
            books.append(bookstore['book'][key])
    return books