def create_bookstore(name):
    bookstore = {'name': name,
            'author': [],
            'book': [],
            }
    return bookstore        

def add_author(bookstore, name, nationality):
    author = {'name': name,
              'nationality': nationality,
              'id': len(bookstore['author']),
              }
    bookstore['author'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for author in bookstore['author']:
        if author['name'] == name:
            return author

def get_author_by_id(bookstore, author_id):
    for author in bookstore['author']:
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    book = {'title': title,
            'isbn': isbn,
            'author_id': author_id,
            'id': len(bookstore['book']),
            }
    bookstore['book'].append(book)
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['book']:
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['book']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    total_books = []
    for book in bookstore['book']:
        if book['author_id'] == author_id:
            total_books.append(book)
    return total_books