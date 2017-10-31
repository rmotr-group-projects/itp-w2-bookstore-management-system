import pprint

def create_bookstore(name):
    return {
    'name' : name,
    'authors' : [],
    'books' : [],
    'last_author_id': 0,
    'last_book_id': 0,
    }
    

def add_author(bookstore, name, nationality):
    dict1 = {}
    dict1['nationality'] = nationality
    dict1['name'] = name 
    Iden = bookstore['last_author_id'] + 1
    dict1['id'] = Iden
    bookstore['authors'].append(dict1)
    bookstore['last_author_id'] += 1
    return dict1
    
def get_author_by_name(bookstore, name):
    list_authors = bookstore.get('authors')
    for i in list_authors:
        if i['name'] == name:
            return i
    return "Sorry author not found"

def get_author_by_id(bookstore, author_id):
    list_ids = bookstore.get('authors')
    for i in list_ids:
        if i['id'] == author_id:
            return i
    return "Sorry author not found"
            
def add_book(bookstore, title, isbn, author_id):
    dict2 = {}
    dict2['title'] = title
    dict2['isbn'] = isbn 
    author = get_author_by_id(bookstore, author_id)
    authorsid = author['id']
    authorsname = author['name']
    dict2['author_id'] = authorsid
    dict2['author'] = authorsname
    Iden = bookstore['last_book_id'] + 1
    dict2['id'] = Iden
    bookstore['books'].append(dict2)
    bookstore['last_book_id'] += 1
    return dict2
    
def get_book_by_title(bookstore, title):
    list_books = bookstore.get('books')
    for i in list_books:
       if i['title'] == title:
            return i
    return "Sorry book not found"
    
def get_book_by_id(bookstore, book_id):
    list_ids = bookstore.get('books')
    for i in list_ids:
        if i['id'] == book_id:
            return i
    return "Sorry book not found"
    
def get_books_by_author(bookstore, author_id):
    list_ids = bookstore.get('books')
    total_books = []
    for i in list_ids:
        if i['author_id'] == author_id:
            total_books.append(i)
    return total_books

