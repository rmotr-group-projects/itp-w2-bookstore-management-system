def create_bookstore(name):
    bookstore = {'name': name,'authors' : {}, 'books' : {}}
    return bookstore

def add_author(bookstore, name, nationality):
    # for each new entry move the id up 1
    i = len(bookstore['authors'].keys())
    x = {'name' : name, 'nationality' : nationality, 'id' : i}
    bookstore['authors'][i]= x
    return x

def get_author_by_name(bookstore, name):
    a_id = 0
    for key ,value in bookstore['authors'].items():
        for k, v in value.items():
            if v == name:
                a_id = key
            
    return bookstore['authors'][key]


def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]
    

def add_book(bookstore, title, isbn, author_id):
    book_index = len(bookstore['books'].keys())
    book = {'title' : title, 'isbn' : isbn, 'author_id' : author_id, 'id' : book_index}
    bookstore['books'][book_index]= book
    return book


def get_book_by_title(bookstore, title):
    b_id = 0
    for key ,value in bookstore['books'].items():
        for k, v in value.items():
            if v == title:
                b_id = key
            
    return bookstore['books'][b_id]


def get_book_by_id(bookstore, book_id):
    return bookstore['books'][book_id]
        


def get_books_by_author(bookstore, author_id):
    book = []
    for key ,value in bookstore['books'].items():
        for k, v in value.items():
            if v == author_id and k == 'author_id':
                book.append(bookstore['books'][key])
    return book
