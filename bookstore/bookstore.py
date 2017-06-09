

def create_bookstore(name):
   
    bookstore = {'name': name, 
                 'authors': [], 
                 'books' : [],
                 'author_id' : 0,
                 'book_id' : 0
                }
                
    return bookstore

def add_author(bookstore, name, nationality):
    
    author = {'name': name, 
              'nationality' : nationality, 
              'id' : bookstore['author_id'] 
             }
             
    bookstore['author_id'] += 1
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
        
    #when pass autho_id
    #check bookstore if there
    #if id = id in the bookstore
    #return AUTHOR!!!! NOT ID - I need to read directions more...

def add_book(bookstore, title, isbn, author_id):
    books = {
            'title': title,
            'isbn': isbn,
            'author_id': author_id,
            'id' : bookstore['book_id']
            }
            
    bookstore['book_id'] += 1        
    bookstore['books'].append(books)
    return books

def get_book_by_title(bookstore, title):
    for books in bookstore['books']:
        if books['title'] == title:
            return books


def get_book_by_id(bookstore, book_id):
    for books in bookstore['books']: 
        if books['id'] == book_id:
            return books

def get_books_by_author(bookstore, author_id):
    requested_books = []
    for book in bookstore['books']: 
        if book['author_id'] == author_id:
            requested_books.append(book)
    return requested_books        
