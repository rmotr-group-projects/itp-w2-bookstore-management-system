def create_bookstore(name):
    store = {
        'name': name,
        'authors': [],
        'books': [],
    }
    return store

def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality, 
    }
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    author_list = bookstore['authors']
    
    for author in author_list:
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
    book_list = bookstore['books']
    
    for book in book_list:
        if title == book['title']:
            return book


def get_books_by_author(bookstore, author):
    books = []
    
    book_list = bookstore['books']
    for book in book_list:
        if author == book['author']:
            books.append(book)
            
    return books

'''
bookstore = {
    'name': 'rmotr's bookstore',
    'authors': [
        {
            'name': 'Edgar Allan Poe',
            'nationality': 'US'
        },
        {
            'name': 'Jorge Luis Borges',
            'nationality': 'AR'
        },
        {
            'name': 'James Joyce',
            'nationality': 'UK'
        }
    ]
    'books': [
        # each item in this list is a dictionary
        El Aleph, 
        The Raven, 
        Ulysses, 
        Ficctiones
    ]
}
'''