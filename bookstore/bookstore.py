def create_bookstore(name):

    bookstore = { 'name' : name, 
                  'authors' : [], 
                  'books' : []
                }
    return bookstore

def add_author(bookstore, name, nationality):
    _id = id(name)
    author = {'name' : name, 
              'nationality' : nationality, 
              'id' : _id}
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    authors = bookstore['authors']
    for author in authors:
        if author['name'] == name:
            break
    return author

def get_author_by_id(bookstore, author_id):
    authors = bookstore['authors']
    for author in authors:
        if author_id == author['id']:
            break
    return author

def add_book(bookstore, title, isbn, author_id):
    _id = id(isbn)
    book = {'title' : title, 
            'isbn' : isbn, 
            'author_id' : author_id,
            'id': _id
            }
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    books = bookstore['books']
    for book in books:
        if book['title'] == title:
            break
    return book

def get_book_by_id(bookstore, book_id):
    books = bookstore['books']
    for book in books:
        if book_id == book['id']:
            break
    return book

def get_books_by_author(bookstore, author_id):
    books = bookstore['books']
    books_by_author = []
    for book in books:
        if book['author_id'] == author_id:
            books_by_author.append(book)
    return books_by_author
    