def create_bookstore(name):
    name = {}
    name['authors'] = []
    name['books'] = []
    return name


def get_bookstore_name(bookstore):
    bookstore['name'] = "rmotr's bookstore"
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):#return author dict
    find_author = name
    for author in bookstore['authors']:
        if author['name'] == find_author:
            return author

def add_book(bookstore, title, isbn, author):
    book = {
        'title': title,
        'isbn' : isbn,
        'author': author
    }
    bookstore['books'].append(book)


def get_book_by_title(bookstore, title):
    find_book = title
    for book in bookstore['books']:
        if book['title'] ==  find_book:
            return book


def get_books_by_author(bookstore, author):
    find_book_author = author
    author_book_list = []
    for book in bookstore['books']:
        if book['author'] == find_book_author:
            author_book_list.append(book)
    return author_book_list
    