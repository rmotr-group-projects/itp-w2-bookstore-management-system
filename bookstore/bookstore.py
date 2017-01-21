def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors': [],
        'books': []
    }
    return bookstore

def add_author(bookstore, name, nationality):
    author_id = len(bookstore['authors'])+1
    author = {
        'name':name,
        'nationality':nationality,
        'id':author_id,
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for x in bookstore['authors']:
        if x['name'] == name:
            return x

def get_author_by_id(bookstore, author_id):
    for x in bookstore['authors']:
        if x['id'] == author_id:
            return x

def add_book(bookstore, title, isbn, author_id):
    book_id = len(bookstore['books'])+1000000
    book = {
        'title' : title,
        'isbn' : isbn,
        'author_id' : author_id,
        'id' : book_id
    }
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    for x in bookstore['books']:
        if x['title'] == title:
            return x


def get_book_by_id(bookstore, book_id):
    for x in bookstore['books']:
        if x['id'] == book_id:
            return x


def get_books_by_author(bookstore, author_id):
    books = []
    for x in bookstore ['books']:
        if x['author_id'] == author_id:
            books.append(x)
    return books