def create_bookstore(name):
    store = {'name' : name,
            'authors' : {},
            'books' : {},
            'author_id' : 0,
            'book_id' : 0
    }
    return store

def add_author(bookstore, name, nationality):
    author = {}
    author["name"] = name
    author["nationality"] = nationality 
    author['id'] = bookstore['author_id']
    bookstore['author_id'] += 1
    bookstore['authors'][name] = author
    return author
    
def get_author_by_name(bookstore, name):
    for author_name, author in bookstore['authors'].items():
      if author['name'] is name:
       return author


def get_author_by_id(bookstore, author_id):
    for author_name, author in bookstore['authors'].items():
      if author['id'] == author_id:
       return author


def add_book(bookstore, title, isbn, author_id):
    book = {}
    book["title"] = title
    book["isbn"] = isbn 
    book['id'] = bookstore['book_id']
    book['author_id'] = author_id
    bookstore['book_id'] += 1
    bookstore['books'][title] = book
    return book


def get_book_by_title(bookstore, title):
    for book_name, book in bookstore['books'].items():
        if book['title'] is title:
            return book


def get_book_by_id(bookstore, book_id):
    for book_name, book in bookstore['books'].items():
       if book['id'] is book_id:
           return book
       


def get_books_by_author(bookstore, author_id):
    bookslist = []
    for book_name, book in bookstore['books'].items():
      if book['author_id'] is author_id:
          bookslist.append(book)
    return bookslist
        

# PYTHONPATH=. py.test tests/test_bookstore.py::BookstoreTestCase::test_add_get_authors