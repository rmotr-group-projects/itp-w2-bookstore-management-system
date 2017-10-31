"""
from hints below.
def create_bookstore(name):
    return {
        'name': name,
        'last_author_id': 0,
        'last_book_id': 0,
        'books': [],
        'authors': []
    }
"""


def create_bookstore(name):
    bookstore = {
        'name': name, 'authors': [], 'books': [], 'author_id': 0, 'book_id': 0}
    return bookstore


#
# From hints -
# def add_author(bookstore, name, nationality):
#    bookstore['last_author_id'] += 1
#    author = {
#        'name': name,
#        'nationality': nationality,
#        'id': bookstore['last_author_id']
#    }
#    bookstore['authors'].append(author)
#    return author
#


def add_author(bookstore, name, nationality):
    author = {'name': name, 'nationality': nationality, 'id': bookstore['author_id']}
    bookstore['author_id'] += 1
    bookstore['authors'].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if name == author['name']:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author_id == author['id']:
            return author


#
# Use the same method as authors to auto increase the book ID count.Increment by 1
#


def add_book(bookstore, title, isbn, author_id):
    book = {'title': title, 'isbn': isbn, 'author_id': author_id, 'id': bookstore['book_id']}
    bookstore['book_id'] += 1
    bookstore['books'].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if title == book['title']:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book_id == book['id']:
            return book


def get_books_by_author(bookstore, author_id):
    books_by_author_list = []
    for book in bookstore['books']:
        if author_id == book['author_id']:
            books_by_author_list.append(book)
    return books_by_author_list
