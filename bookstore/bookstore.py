def create_bookstore(name):
    
    # initializes bookstore dict, populates with name (taking name input).
    # also creates lists for authors and books, needed later
    # initializes author_id and book_id to be incremented later
    
    bookstore = {
        'name': name,
        'authors' : [],
        'books' : [],
        'author_id' : 0,
        'book_id' : 0
    }
    
    # returns bookstore once complete
    
    return bookstore
    

def add_author(bookstore, name, nationality):
    
    # initialize the author dict, containing name (takes input), nationality
    # (takes input), and id which is pulled from the original bookstore object. 
    
    author = {
        'name' : name,
        'nationality' : nationality,
        'id' : bookstore['author_id']
    }
    
    # increments the author_id counter by 1 to give each author a unique id
    # to be used later.
    
    bookstore['author_id'] += 1
    
    # appends the author dict to the authors list inside the bookstore dict.
    # creates a list of dicts inside the dict
    
    bookstore['authors'].append(author)
    
    # returns the author dict that was just created for the current author
    
    return author
    

def get_author_by_name(bookstore, name):
    
    # a for loop which looks through the authors dict in the bookstore dict to
    # find an author that equals the 'name' passed in the function.
    # once found, returns the author dict.
    
    for author in bookstore['authors']:
        if name == author['name']:
            return author
    

def get_author_by_id(bookstore, author_id):
    
    # works like author_by_name function, but for id. once found, returns author
    
    for author in bookstore['authors']:
        if author_id == author['id']:
            return author


def add_book(bookstore, title, isbn, author_id):
    
    # initialize the author dict, containing title (takes input), isbn number
    # (takes input), and id which is pulled from the original bookstore object. 
    
    book = {
        'title' : title,
        'isbn' : isbn,
        'author_id' : author_id,
        'id' : bookstore['book_id']
    }
    
    # increments the book_id counter by 1 to give each book a unique id
    # to be used later.
    
    bookstore['book_id'] += 1
    
    # appends the book dict to the books list inside the bookstore dict.
    # creates a list of dicts inside the dict
    
    bookstore['books'].append(book)
    
    # returns the book dict that was created with function
    
    return book 


def get_book_by_title(bookstore, title):
    
    # a for loop which looks through the books dict in the bookstore dict to
    # find an title that equals the 'title' passed in the function.
    # once found, returns the book dict.
    
    for book in bookstore['books']:
        if title == book['title']:
            return book


def get_book_by_id(bookstore, book_id):
    
    # works like book_by_title function, but for id. once found, returns book
    
    for book in bookstore['books']:
        if book_id == book['id']:
            return book 


def get_books_by_author(bookstore, author_id):
    
    # this one works a little differently, because there could be multiple books
    # from the same author. accordingly, this function creates a new list,
    # and appends each book in the bookstore['books'] list that corresponds
    # to that author, to the new list.
    
    books_return_list = []
    
    for book in bookstore['books']:
        if author_id == book['author_id']:
            books_return_list.append(book)
    
    # returns the new books_return_list list 
    
    return books_return_list
