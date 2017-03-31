import random




# """
# store = {'poe': , 'blah1': ,'blah2'} 
# store['authors']['Poe'] = { 'name': 'Edgar allen pow', etc. }

# bookstore which is a dictionary
# bookstore = {
#     'name' : 'rmotr bookstore'
#     'authors' : { 
#         'Poe' : { 'name' : 'Edgar Allen Poe', 'id' : 1, 'nationality' : 'US' },
#         'Blah' : { 'name' : 'other name', 'id' : 2, 'nationality': 'AR' },
#         'Blah2' : { 'name' : 'last person', 'id' : 3, 'nationality' : 'UK' }
#     },
#     'books' : { 
        
#     }
# }

# bookstore['authors']['Poe']['name'] >> 'edgar allen poe'

# """

def create_bookstore(name):
    bookstore = {'authors': [],
                 'author_id': 1,
                 'books': [],
                 'book_id': 1
    }
    bookstore['name'] = name
    return bookstore

def add_author(bookstore, name, nationality):
    author_dict = { 'name' : name,
               'nationality' : nationality,
               'id': bookstore['author_id'],
    }
    bookstore['author_id'] += 1
    bookstore['authors'].append(author_dict)
    return author_dict

def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author

def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    book_dict = { 'title': title,
                  'isbn' : isbn,
                  'id' : bookstore['book_id'],
                  'author_id' : author_id
    }
        
    bookstore['book_id'] += 1
    bookstore['books'].append(book_dict)
    return book_dict

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book
        
        
def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    books_by_author = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            books_by_author.append(book)
    return books_by_author
        
