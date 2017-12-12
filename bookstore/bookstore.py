def create_bookstore(name):
    bookstore = {'store': name, 'author': [], 'books': [] }
    return bookstore

def get_bookstore_name(bookstore):
    return bookstore['store']


def add_author(bookstore, name, nationality):
    author = {'name':name, 'nationality':nationality}
    bookstore['author'].append(author)

    return author

def get_author_by_name(bookstore, name):
    for author in bookstore['author']:
        if name == author['name']:
            return author


def add_book(bookstore, title, isbn, author):
    book = {'isbn':isbn, 'title':title, 'author':author}
    bookstore['books'].append(book)
    
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if title == book['title']:
            return book


def get_books_by_author(bookstore, author):
    authors_book_list = []
    
    for book_author in bookstore['books']:
        if author == book_author['author']:
            authors_book_list.append(book_author)

    return authors_book_list