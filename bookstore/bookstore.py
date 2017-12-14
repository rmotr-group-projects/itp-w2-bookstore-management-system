def create_bookstore(name):
    return {
        'name': name,
        'books': [],
        'authors': [],
        'author_id': 0,
        'book_id': 0
    }


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {'name':name, 'nationality':nationality}
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
    
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return title


def get_books_by_author(bookstore, author):
    result = []
    for book in bookstore['books']:
        if book['author'] == author:
            result.append(author)
    
    return result
    
