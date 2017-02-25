def create_bookstore(name):
    store = {'name': name,
            'books': [],
            'author': [],
            'id_count': 0,
            'book_count': 0,
    }
    return store

    
def add_author(bookstore, name, nationality):
    author  = {'name': name,
            'nationality': nationality,
            'id': bookstore['id_count'],
     }
    bookstore['author'].append(author)
    bookstore['id_count'] += 1
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['author']:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    
    for author in bookstore['author']:
        if author_id == author['id']: 
            return author

            
def add_book(bookstore, title, isbn, author_id):
    add_books = { 'title': title,
             'isbn': isbn,
             'id': bookstore['book_count'],
             'author_id': author_id,
             }
    bookstore['books'].append(add_books) 
    bookstore['book_count'] += 1 
    return add_books


def get_book_by_title(bookstore, title):
    for add_books in bookstore['books']:
        if add_books['title'] == title:
            return add_books


def get_book_by_id(bookstore, book_id):
    for add_books in bookstore['books']:
        if book_id == add_books['id']:
            return add_books


def get_books_by_author(bookstore, author_id):
    book_lst = []
    for n in bookstore['books']: 
        if n['author_id'] == author_id: 
            book_lst.append(n)
    return book_lst
