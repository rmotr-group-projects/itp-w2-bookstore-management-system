

def create_bookstore(name):
    store = {}
    store['name'] = name
    store['authors'] = {}
    store['books'] = {}
    return store

#print(create_bookstore('Fake Name'))


def add_author(bookstore, name, nationality):
    #bookstore['id'] += 1
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    #author['id'] = bookstore['id']
    author['id'] = name + nationality
    bookstore['authors'][name] = author
    return author

# bookstore['authors'][key] = author

def get_author_by_name(bookstore, name):
    for author in bookstore['authors'].values():
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors'].values():
        if author['id'] == author_id:
            return author


def add_book(bookstore, title, isbn, author_id):
    book = {}
    book['title'] = title
    book['isbn'] = isbn
    book['id'] = title + isbn
    book['author_id'] = author_id
    bookstore['books'][title] = book
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books'].values():
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books'].values():
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    book_list = []
    for book in bookstore['books'].values():
        if book['author_id'] == author_id:
            book_list.append(book)
    return book_list