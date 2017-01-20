def create_bookstore(name):
    return {'name':name,
            'author':[],
            'book':[],
            'init_author_id':0,
            'init_book_id':1000000}

def add_author(bookstore, name, nationality):
    bookstore['init_author_id'] += 1
    author = {'name':name,
              'nationality':nationality,
              'id':bookstore['init_author_id']}
              
    bookstore['author'].append(author)          
              
    return author

def get_author_by_name(bookstore, name):
    for a in bookstore['author']:
        if a['name'] == name:
            return a

def get_author_by_id(bookstore, author_id):
    for a in bookstore['author']:
        if a['id'] == author_id:
            return a

def add_book(bookstore, title, isbn, author_id):
    bookstore['init_book_id'] += 1
    book = {'title':title,
            'isbn':isbn,
            'author_id':author_id,
            'id':bookstore['init_book_id']}
    bookstore['book'].append(book)
    
    return book

def get_book_by_title(bookstore, title):
    for b in bookstore['book']:
        if b['title'] == title:
            return b

def get_book_by_id(bookstore, book_id):
    for b in bookstore['book']:
        if b['id'] == book_id:
            return b

def get_books_by_author(bookstore, author_id):
    books=[]
    for b in bookstore['book']:
        if b['author_id'] == author_id:
            books.append(b)
    
    return books
