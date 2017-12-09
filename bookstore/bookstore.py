def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors': [],
        'books': []
    }
    return bookstore


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality
    }
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author


def add_book(bookstore, title, isbn, author):
    pass


def get_book_by_title(bookstore, title):
    pass


def get_books_by_author(bookstore, author):
    pass
