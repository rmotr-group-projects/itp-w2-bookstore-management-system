def create_bookstore(name):
    bookstore = {}
    bookstore['bookstore name'] = name
    bookstore['authors'] = [] #makes an empty list for authors
    bookstore['books'] = [] #makes an empty list for books
    return bookstore


def get_bookstore_name(bookstore):
    return bookstore['bookstore name']



def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality
    }
    bookstore['authors'].append(author)
    return author
    

def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        'title': title,
        'isbn': isbn,
        'author': author
    }
    bookstore['books'].append(book)
    return bookstore
    


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_books_by_author(bookstore, author):
    result = []
    for book in bookstore['books']:
        if book['author'] == author:
            result.append(book)
    return result