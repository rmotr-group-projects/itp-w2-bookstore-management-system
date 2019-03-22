def create_bookstore(name):
    return {
        'name': name,
        'authors': [],
        'books': [],
    }


def get_bookstore_name(bookstore):
    return bookstore['name']


def add_author(bookstore, name, nationality):
    author = {
        'name': name,
        'nationality': nationality,
    }
    bookstore['authors'].append(author)
    
    return author


def get_author_by_name(bookstore, name):
    authors = bookstore['authors']
    
    for author_dict in authors:
        if author_dict['name'] == name:
            return author_dict


def add_book(bookstore, title, isbn, author):
    book = {
        'title': title,
        'isbn': isbn,
        'author': author
    }
    bookstore['books'].append(book)
    
    return book


def get_book_by_title(bookstore, title):
    books = bookstore['books']
    
    for book in books:
        if book['title'] == title:
            return book


def get_books_by_author(bookstore, author):
    results = []
    books = bookstore['books']
    
    for book in books:
        if book['author'] == author:
            results.append(book)
            
    return results