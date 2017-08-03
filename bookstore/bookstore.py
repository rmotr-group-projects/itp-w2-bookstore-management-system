def create_bookstore(name):
    return {
        'name': name,           # this will not change
        'last_author_id': 0,    # counter
        'last_book_id': 0,      # counter
        'books': [],            # list of dicts
        'authors': []           # list of dicts
    }

def add_author(bookstore, name, nationality):           # each author is a dict
    bookstore['last_author_id']+=1
    newauthor = {'name': name, 'nationality': nationality, 'id': bookstore['last_author_id']}
    bookstore['authors'].append(newauthor)
    return newauthor
    """future versions should include checking to be sure author's dictionary matches what's already in the system."""


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author
    else:
        return None


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author
    else:
        return None


def add_book(bookstore, title, isbn, author_id):            # each book is a dict
    bookstore['last_book_id']+=1
    newbook = {'title': title, 'isbn': isbn, 'author_id': author_id, 'id': bookstore['last_book_id']}
    bookstore['books'].append(newbook)
    return newbook
    """future versions should include checking to be sure book's dictionary matches what's already in the system."""


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book
    else:
        return None

def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book
    else:
        return None


def get_books_by_author(bookstore, author_id):
    books = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            books.append(book)
    return books
