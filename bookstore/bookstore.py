import time

def create_bookstore():
    name = {}
    return name

def add_author(bookstore, name, nationality):

    my_time = time.time()
    
    my_dic = {}
    new_author = {
            'name' : name, 
            'nationality' : nationality,
            'id' : my_time, 
            'books' : my_dic
        }

    bookstore[name] = new_author

    

    return bookstore[name]


def get_author_by_name(bookstore, name):
    pass


def get_author_by_id(bookstore, author_id):
    pass


def add_book(bookstore, title, isbn, author_id):
    
    book_id = time.time()

    for i in bookstore : 
        if bookstore[i]['id'] == author_id : 
            book = {

                #'title' : title,
                'isbn' : isbn,
                'id' : book_id

            }

            bookstore[i]['books'][title] = book 
    return bookstore[i]['books'][title]


def get_book_by_title(bookstore, title):
    pass


def get_book_by_id(bookstore, book_id):
    pass


def get_books_by_author(bookstore, author_id):
    pass