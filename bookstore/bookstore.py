def create_bookstore(name):
    name = {'name':  name, 'authors': {}, 'books': {}}
    return name

def add_author(bookstore, name, nationality):
    author_id = len(bookstore['authors']) + 10
    bookstore['authors'][author_id] = {'name': name, 'nationality': nationality, 'id': author_id, 'books': []}
    return bookstore['authors'][author_id]


def get_author_by_name(bookstore, name):
    for i in range(10, len(bookstore['authors']) + 10):
        for keys, names in bookstore['authors'][i].items():
            if names == name:
                return bookstore['authors'][i]


def get_author_by_id(bookstore, author_id):
    for i in range(10, len(bookstore['authors']) + 10):
        for keys, ids in bookstore['authors'][i].items():
            if ids == author_id:
                return bookstore['authors'][i]


def add_book(bookstore, title, isbn, author_id):
    book_id = len(bookstore['books'])
    bookstore['books'][book_id] = {'title': title, 'isbn': isbn, 'id': book_id, 'author_id': author_id}
    return bookstore['books'][book_id]


def get_book_by_title(bookstore, title):
    for i in range(len(bookstore['books'])):
        for keys, titles in bookstore['books'][i].items():
            if titles == title:
                return bookstore['books'][i]


def get_book_by_id(bookstore, book_id):
    for i in range(len(bookstore['books'])):
        for keys, ids in bookstore['books'][i].items():
            if ids == book_id:
                return bookstore['books'][i]


def get_books_by_author(bookstore, author_id):
    results = []
    for i in range(len(bookstore['books'])):
        for keys, ids in bookstore['books'][i].items():
            if ids == author_id:
                results.append(bookstore['books'][i])
    return results