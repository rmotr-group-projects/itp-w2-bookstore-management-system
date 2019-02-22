def create_bookstore(name):
    return {
        'bookstore name': name,
        'authors': [],
        'books': [],
    }


def get_bookstore_name(bookstore):
    return bookstore['bookstore name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
    }
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if name == author['name']:
            return author

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
        if title == book['title']:
            return book


def get_books_by_author(bookstore, author):
    authors_books = []
    for person in bookstore['books']:
        if author == person['author']:
            authors_books.append(person)
    return authors_books
 
