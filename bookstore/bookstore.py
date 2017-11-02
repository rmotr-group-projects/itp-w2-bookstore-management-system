import uuid  # module to generate random uuid's

# store object design
# store = {
#     'name': 'store name', # good
#     'authors': [
#         'author1': {
#             'id': '12345',
#             'name': 'name1',
#             'nationality': 'US',
#             'books': [
#                 'book1': {
#                     'id': '12345',
#                     'title': 'book title',
#                     'isbn': '12345555555',
#                     'author_id': 'author_id1'
#                 }
#             ]
#         }
#     ]
# }

def create_id():
    return str(uuid.uuid4())


def create_bookstore(name):
    store = {}
    store.setdefault('store_id', create_id())
    store.setdefault('name', name)

    return store    


def add_author(bookstore, name, nationality):
    store = bookstore
    store.setdefault('authors', [])

    authors = store.get('authors')

    author = {
        'id': create_id(),
        'name': name,
        'nationality': nationality
    }

    authors.append(author)

    for author in store['authors']:
        if author['name'] == name:
            return author


def get_author_by_name(bookstore, name):
    store = bookstore
    authors = store.get('authors')
    
    for author in authors:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    store = bookstore
    authors = store.get('authors')

    for author in authors:
        if author['id'] == author_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    store = bookstore
    author = get_author_by_id(bookstore, author_id)
    author.setdefault('books', [])
    books = author.get('books')

    book = {
        'title': title,
        'isbn': isbn,
        'id': create_id(),
        'author_id': author_id
    }

    books.append(book)

    return book


def get_book_by_title(bookstore, title):
    store = bookstore
    authors = store.get('authors')

    for author in authors:
        books = author['books']

        for book in books:
            if book['title'] == title:
                return book


def get_book_by_id(bookstore, book_id):    
    store = bookstore
    authors = store.get('authors')

    for author in authors:
        books = author.get('books')

        for book in books:
            if book['id'] == book_id:
                return book

def get_books_by_author(bookstore, author_id):
    store = bookstore
    authors = store.get('authors')

    for author in authors:
        if author['id'] == author_id:
            return author['books']
