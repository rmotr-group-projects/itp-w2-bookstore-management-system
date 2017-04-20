def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors':[],
        'books': [],
        'author_id': 0,
        'book_id': 0
    }
    return bookstore

    
def add_author(bookstore, name, nationality):
    
    author = {
        'name':  name,
        'id' : bookstore['author_id'] ,     
        'nationality': nationality
    }
    bookstore['author_id'] += 1
    bookstore['authors'].append(author)
    return author
    
    
    
def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if name == author['name']:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author_id == author['id']:
            return author


def add_book(bookstore, title, isbn, author_id):
    book = {'title': title,
    'isbn': isbn,
    'author_id': author_id,
    'id': bookstore['book_id']
    
    }
    bookstore['book_id'] += 1
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    
    for book in bookstore['books']:
        if title == book['title']:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book_id == book['id']:
            return book


def get_books_by_author(bookstore, author_id):
    authorlist = []
    for book in bookstore['books']:
        if author_id == book['author_id']:
            authorlist.append(book)
    return authorlist


