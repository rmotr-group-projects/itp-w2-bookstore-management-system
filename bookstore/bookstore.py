def create_bookstore(name):
    return {
        'name': name,
        'authors': [],
        'books': [],
    }

'''
bookstore = {
    'name': "rmotr's bookstore",
    'authors': [
        {
        'name': 'Edgar Allen Poe',
        'nationality': 'US',
        'books': [...]
        },
        {
        'name': 'Jorge Luis Borges',
        'nationality': 'AR',
        'books': [...]
        },
        {
        'name': "James Joyce",
        'nationality', 'UK',
        'books': [...]
        },
    ]
    'books': [...]
}
'''


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
        'books': []
    }
    
    bookstore['authors'].append(author)
    
    return author
    


def get_author_by_name(bookstore, name):
    author_list = bookstore['authors']
    
    for author in author_list:
        if author['name'] == name:
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        'title': title,
        'isbn': isbn,
        'author': author,
    }
    
    author_list = bookstore['authors']
    for writer in author_list:
        if writer['name'] == author:
            writer['books'].append(book)
            
    bookstore['books'].append(book)
            
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book
        


def get_books_by_author(bookstore, author):
    
    for writer in bookstore['authors']:
        if writer['name'] == author:
            return writer['books']
