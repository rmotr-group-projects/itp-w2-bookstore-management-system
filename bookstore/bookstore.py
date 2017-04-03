
def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors': [],
        'books': [],
        'last_author_id': 0,
        'last_book_id': 100
            }
    return bookstore

def add_author(bookstore, name, nationality):
    bookstore['last_author_id'] += 1
    author = {
        'name': name,
        'id': bookstore['last_author_id'],
        'nationality': nationality
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    count = 0
    for dic in bookstore['authors']:
        if dic['name'] == name:
            return bookstore['authors'][count]
        count += 1


def get_author_by_id(bookstore, author_id):
    count = 0
    for dic in bookstore['authors']:
        if dic['id'] == author_id:
            return bookstore['authors'][count]
        count += 1

def add_book(bookstore, title, isbn, author_id):
    bookstore['last_book_id'] += 1
    book = {
        'title': title,
        'id': bookstore['last_book_id'],
        'isbn': isbn,
        'author_id': author_id,
    }
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    count = 0
    for dic in bookstore['books']:
        if dic['title'] == title:
            return bookstore['books'][count]
        count += 1


def get_book_by_id(bookstore, book_id):
    count = 0
    for dic in bookstore['books']:
        if dic['id'] == book_id:
            return bookstore['books'][count]
        count += 1

def get_books_by_author(bookstore, author_id):
    author_books = []
    search_id = author_id
    for book in bookstore['books']:
        if book['author_id'] == search_id:
            author_books.append(book)
    return author_books
