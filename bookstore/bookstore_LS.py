#auto-increment integer ID
def create_bookstore(name):
    return {
        'name': name,
        'last_author_id': 0,
        'last_book_id': 0, # here was the missing comma earlier
        'authors': [],
        'books': [],
    }
    
#add this "author" to the list of `authors` in the bookstore with name, nationality and id
def add_author(bookstore, name, nationality):
    bookstore['last_author_id'] += 1
    author = {
        'name': name,
        'nationality': nationality,
        'id': bookstore['last_author_id']
    }
    
    bookstore['authors'].append(author)
    return author


#Loop searching for string "authors", return author name
def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author

#Loop searching for author id match, return author name
def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author
            
#add this "book" to the list of `books` in the bookstore with title, isbn, author id,and id
def add_book(bookstore, title, isbn, author_id):
    bookstore['last_book_id'] += 1
    book = {
        'title': title,
        'isbn': isbn,
        'author_id': author_id,
        'id': bookstore['last_book_id']
    }
    bookstore['books'].append(book)
    return book

#Loop search for title match
def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book

#Loop search for book isbn match
def get_book_by_id(bookstore, book_isbn):
    for book in bookstore['books']:
        if book['id'] == book_isbn:
            return book

#Loop search for book author id match
def get_books_by_author(bookstore, author_id):
    books = []
    
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            books.append(book)
    
    return books
