#helper functions
def create_bookstore(name):
    bookstore = {
        'shop_name':name,
        'authors':[],
        'books':[]
    }
    return bookstore


def get_bookstore_name(bookstore):
    return bookstore['shop_name']
    

def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
        'books':[]
    }
    
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if name.lower() in author['name'].lower():
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        'title':title,
        'isbn':isbn,
        'author':author
    }
    bookstore['books'].append(book)
    
    for writer in bookstore['authors']:
        if author.lower() in writer['name'].lower():
            writer['books'].append(book)
    
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if title.lower() in book['title'].lower():
            return book


def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore['books']:
        if author.lower() in book['author'].lower():
            books.append(book)
    return books
