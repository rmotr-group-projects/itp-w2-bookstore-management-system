

def create_bookstore(name):
    return {'name':name,
            'authors': [],
            'books':[]
    }


def add_author(bookstore, name, nationality):
    author = {'id':len(bookstore['authors']),
            'name' : name,
            'nationality': nationality
            }
    bookstore['authors'].append(author)
    return author
    
def get_author_by_name(bookstore, name):
    for elem in range(len(bookstore['authors'])):
        if bookstore['authors'][elem]['name']==name:
            return bookstore['authors'][elem]


def get_author_by_id(bookstore, author_id):
    for elem in range(len(bookstore['authors'])):
        if bookstore['authors'][elem]['id']==author_id:
            return bookstore['authors'][elem]


def add_book(bookstore, title, isbn, author_id):
    book = {'title' : title,
            'isbn' : isbn,
            'author_id': author_id,
             'id' : len(bookstore['books'])
            }   
    bookstore['books'].append(book)
    return book        


def get_book_by_title(bookstore, title):
    for elem in range(len(bookstore['books'])):
        if bookstore['books'][elem]['title']==title:
            return bookstore['books'][elem]


def get_book_by_id(bookstore, book_id):
    for elem in range(len(bookstore['books'])):
        if bookstore['books'][elem]['id']==book_id:
            return bookstore['books'][elem]



def get_books_by_author(bookstore, author_id):
    books = []
    for elem in range(len(bookstore['books'])):
        if bookstore['books'][elem]['author_id']==author_id:
            books.append(bookstore['books'][elem])
    return books
