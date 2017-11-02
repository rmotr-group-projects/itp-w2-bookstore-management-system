def create_bookstore(name):
    return {
        'name': name,
        'authors': [],
        'books': [],
        'last_author_id': 0,
        'last_book_id': 0
    }

def add_author(bookstore, name, nationality):
     bookstore['last_author_id'] += 1
     author = {
        'name': name,
        'nationality': nationality,
        'id': bookstore['last_author_id']
    }
     bookstore['authors'].append(author)

     return author


def get_author_by_name(bookstore, name):
    authors = bookstore.get('authors')
    for author in authors:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    authors = bookstore.get('authors')
    for author in authors:
        if author['id'] == author_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    bookstore['last_book_id'] += 1
    book = {
        'title': title,
        'author_id': author_id,
        'isbn': isbn,
        'id': bookstore['last_book_id']
    }
    bookstore['books'].append(book)
    
    return book


def get_book_by_title(bookstore, title):
    books = bookstore.get('books')
    for book in books:
        if book['title'] == title:
            return book
        

def get_book_by_id(bookstore, book_id):
    books = bookstore.get('books')
    for book in books:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    books_list = []
    books = bookstore.get('books')
    for book in books:
        if book['author_id'] == author_id:
            books_list.append(book)
    return books_list        
