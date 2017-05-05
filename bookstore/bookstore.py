def create_bookstore(name):
    return {
        'name' : name,
        'authors' : [],
        'books': [],
        'author_index' : 0,
        'book_index' : 0
    }

def add_author(bookstore, name, nationality):
    bookstore['author_index'] += 1
    author = {
        'name' : name,
        'nationality' : nationality,
        'id' : bookstore['author_index'],
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for author in bookstore.get('authors'):
        if author['name'] == name:
            return author
            
def get_author_by_id(bookstore, author_id):
    for author in bookstore.get('authors'):
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    bookstore['book_index'] += 1
    book = {
        'title' : title,
        'isbn' : isbn,
        'author_id' : author_id,
        'id' :  bookstore['book_index']
        
    }
    bookstore['books'].append(book)
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore.get('books'):
        if book['title'] == title:
            return book  

def get_book_by_id(bookstore, book_id):
    for book in bookstore.get('books'):
        if book['id'] == book_id:
            return book

def get_books_by_author(bookstore, author_id):
    books = []
    for book in bookstore.get('books'):
        if book['author_id'] == author_id:
            books.append(book)
    return books

