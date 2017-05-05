def create_bookstore(name):
    bookstore = {}
    bookstore['name'] = name
    bookstore['authors'] = []
    bookstore['books'] = []
    bookstore['author_index'] = 0
    bookstore['book_index'] = 0
    return bookstore

def add_author(bookstore, name, nationality):
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    bookstore['author_index'] += 1
    author['id'] = bookstore['author_index']
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore.get('authors'):
        if author['name'] == name:
            return author
            
def get_author_by_id(bookstore, author_id):
    for author in bookstore.get('authors'):
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    book = {}
    book['title'] = title
    book['isbn'] = isbn
    bookstore['book_index'] += 1
    book['id'] = bookstore['book_index']
    book['author_id'] = author_id
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore.get('books'):
        if book['title'] == title:
            return book  


def get_book_by_id(bookstore, book_id):
    for book in bookstore.get('books'):
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    books = []
    for book in bookstore.get('books'):
        if book['author_id'] == author_id:
            books.append(book)
    return books

