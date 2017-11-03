def create_bookstore(name):
    return {
        'name': name,
        'last_author_id': 0,
        'last_book_id': 0,
        'books': [],
        'authors': []
    }

def add_author(bookstore, name, nationality):
    bookstore[last_author_id]+=1
    author = {'name': name, 
              'nationality': nationality,
              'id': bookstore['last_author_id'] }
    bookstore['authors'].append(author)
    return bookstore

def get_author_by_name(bookstore, name):
    for name in bookstore['authors']:
        if bookstore['name']==name:
            return author


def get_author_by_id(bookstore, author_id):
    for authord_id in bookstore['authors']:
        if bookstore['id'] == authord_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    bookstore[last_book_id]+=1
    book={'title':title,
          'isbn':isbn,
          'authord_id':authord_id,
          'book_id': bookstore[last_book_id]}
    bookstore.['books'].append(book)


def get_book_by_title(bookstore, title):
    for title in bookstore['books']:
        if bookstore[title]==title:
            return book


def get_book_by_id(bookstore, book_id):
    for book_id in bookstore['books']:
        if bookstore['book_id']==book_id:
            return book


def get_books_by_author(bookstore, author_id):
    books={}
    for authord_id in bookstore['books']:
        if bookstore[authord_id]==authord_id:
           books.append(book)
    return books
        
