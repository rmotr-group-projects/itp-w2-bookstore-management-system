def create_bookstore(name_bookstore): 
    
    #creating a bookstore 
    bookstore = {
        'name': name_bookstore, #creating the name of the bookstore
        'authors': [], #list of authors in the book store
        'author_id': 0,
        'book_list': [], #list of books in the book store
        'book_id': 0
    }
    
    return bookstore

#adds an author of type dictionary to the list of authors in the bookstore
def add_author(bookstore, name_author, nationality_author):
    
    #creating a profile of a single author to be added to the LIST of authors
    author = {
        'name': name_author,
        'nationality': nationality_author,
        'id': bookstore['author_id']
    }
    
    #for the next time an author profile is created, id assigned to author is the next number
    #this puts the list IDs of the authors in a sequential order 
    bookstore['author_id'] += 1 
    
    #insert this author at the end of the list of authors in the bookstore
    bookstore['authors'].append(author)
    
    return author 
    
    
def get_author_by_name(bookstore, name_author):
    
    for author in bookstore['authors']:
        if name_author == author['name']:
            return author
    
    return 'There is no author by that name in the bookstore.'


def get_author_by_id(bookstore, author_id):
    
    for author in bookstore['authors']:
        if author_id == author['id']:
            return author
    
    return 'There is no match with that id number'


def add_book(bookstore, title, isbn, author_id):
    
    book = {
        'title': title,
        'isbn': isbn,
        'author_id': author_id,
        'id': bookstore['book_id']
    }
    
    #add book to bookstore's book list
    bookstore['book_list'].append(book)
    
    #for next time a book is created, its id is something different (sequential ordering)
    bookstore['book_id'] += 1
    
    return book

def get_book_by_title(bookstore, title):
    
    for book in bookstore['book_list']:
        if title == book['title']:
            return book
    
    return 'The book is not in this book store.'


def get_book_by_id(bookstore, book_id):
    
    for book in bookstore['book_list']:
        if book_id == book['id']:
            return book
            


def get_books_by_author(bookstore, author_id):
    
    books_by_author = []
    
    for book in bookstore['book_list']:
        if author_id == book['author_id']:
            books_by_author.append(book)
    
    return books_by_author

