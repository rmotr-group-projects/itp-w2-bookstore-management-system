def create_bookstore(name):
    return {
        'name': name,
        'books': [],
        'authors': []
    }

def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
        'id': 'auth_' + str(len(bookstore['authors']) + 1)
    }
    
    bookstore['authors'].append(author)
    
    return author


def get_author_by_name(bookstore, name):
    for each_auth_dict in bookstore['authors']:
        if each_auth_dict['name'] == name:
            return each_auth_dict
    return "This author is not in system"
    

def get_author_by_id(bookstore, author_id):
    for each_auth_dict in bookstore['authors']:
        if each_auth_dict['id'] == author_id:
            return each_auth_dict
    return "This ID is not in system"
 


def add_book(bookstore, title, isbn, author_id):
    book = {
        'title': title,
        'isbn': isbn,
        'author_id': author_id,
        'id': 'book_' + str(len(bookstore['books']) + 1)
    }
    
    bookstore['books'].append(book)
    
    return book

def get_book_by_title(bookstore, title):
    for each_book_dict in bookstore['books']:
        if each_book_dict['title'] == title:
            return each_book_dict
    return "This book is not in the system"


def get_book_by_id(bookstore, book_id):
    for each_book_dict in bookstore['books']:
        if each_book_dict['id'] == book_id:
            return each_book_dict 
    return "This book is not in the system"



def get_books_by_author(bookstore, author_id):
    books_by_author = []        
    for each_book_dict in bookstore['books']:
      if each_book_dict['author_id'] == author_id:
        books_by_author.append(each_book_dict)
    return books_by_author