

def create_bookstore(name):
    return {
        'name' : name,
        'authors': [],
        'books': [],
        'author_index' : 1000,
        'books_index' : 1
    
       

    }
def add_author(bookstore, name, nationality):

    bookstore['author_index'] += 1
    author = {
        'name' :  name,
        'nationality' : nationality, 
        'id' : bookstore['author_index']
    }    
    bookstore['authors'].append(author)
    return author
    

def get_author_by_name(bookstore, name):
    
    for author in bookstore['authors']:
        if author['name'] == name:
            return author


def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author
    


def add_book(bookstore, title, isbn, author_id):
    bookstore['books_index'] += 1
    books = {  
        'title' : title,
        'isbn' : isbn,
        'author_id' : author_id,
        'id' : bookstore['books_index']
        }
    bookstore['books'].append(books)
    return books


def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    val = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            val.append(book)
    return val
