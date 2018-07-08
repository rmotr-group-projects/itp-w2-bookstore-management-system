def create_bookstore(name):
    return {
        'name' : name,
        'authors' : [],
        'books' : []
    }


def get_bookstore_name(bookstore):
    return bookstore.get("name")

def add_author(bookstore, name, nationality):
    author = {
        'name' : name,
        'nationality' : nationality
    }
    
    bookstore['authors'].append(author)
    
    return author

def get_author_by_name(bookstore, name):
    bookstore_authors = bookstore.get("authors")
    
    for author in bookstore_authors:
        if author.get('name') == name:
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        'title' : title,
        'isbn' : isbn,
        'author' : author
    }
    
    bookstore['books'].append(book)
    
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book.get("title") == title:
            return book


def get_books_by_author(bookstore, author):
    author_books = []
    
    for book in bookstore['books']:
        if book.get("author") == author:
            author_books.append(book)
    return author_books
