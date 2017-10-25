def create_bookstore(name):
    store = {
        'name': name,
        'authors': [],
        'books': []
    }

    return store

def add_author(bookstore, name, nationality):

    id = len(bookstore['authors'])

    author = {
        'id': id + 1,
        'name' : name,
        'nationality' : nationality
    }

    bookstore['authors'].append(author)

    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author

    return None


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author

    return None


def add_book(bookstore, title, isbn, author_id):

    id = len(bookstore['books'])

    book = {
        'id': id + 1,
        'title' : title,
        'isbn' : isbn,
        'author_id' : author_id
    }

    bookstore['books'].append(book)

    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book

    return None


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book

    return None


def get_books_by_author(bookstore, author_id):
    books = []

    for book in bookstore['books']:
        if book['author_id'] == author_id:
            books.append(book)

    return books