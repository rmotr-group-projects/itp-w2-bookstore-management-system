"""
BATUHAN BASERDEM: ITP: Week 2: Group exercise

The proposed data structure is as follows;

BOOKSTORE
|   -Entire store is within a dict with the following attributes
|---*NAME
|       -This contains the name of the bookstore
|       -Is a string
|---*AUTHORS
|   |   -This contains all the authors inside
|   |   -It is a list structure
|   \~~~*SINGLE AUTHORS
|       |   -Single authors are dictionaries with the following keys;
|       |---*NAME
|       |       -Name of the author
|       |---*NATIONALITY
|       |       -Nationality of the author
|       \---*ID
|               -Index used to reach this author
\---*BOOKS
    |   -This contains all the books inside
    |   -It is a list structure
    \~~~*SINGLE BOOKS
        |   -Single books are dictionaries with the following keys;
        |---*TITLE
        |       -Name of the book
        |---*ISBN
        |       -Library code used to denote books
        |---*ID
        |       -Index used to reach this book
        \---*AUTHOR ID
                -The number used to reach the author of this book

End point data is reached as following
bookstore['name']
bookstore['authors'][<int>]['name'/'nationality'/'id']
bookstore['books'][<int>]['title'/'isbn'/'id'/'author_id']
"""

def create_bookstore(name):
    return {'name':name, 'authors':[], 'books':[] }

def add_author(bookstore, name, nationality):
    # Check if there are any authors in the library to begin with
    if not 'authors' in bookstore:
        return 'Invalid bookstore'
    # Put the author here. Len() gives the index of the recently added element
    bookstore['authors'].append( {
        'name':name,
        'nationality':nationality,
        'id':len(bookstore['authors']) } )
    # Return the author by default
    return bookstore['authors'][-1]


def get_author_by_name(bookstore, name):
    # Check authors available
    for author in bookstore['authors']:
        # If the correct author is there, return that author
        if author['name'] == name:
            return author
    # If not found, return the bust string
    return 'Author not in bookstore'


def get_author_by_id(bookstore, author_id):
    # Return error if the book id is not in the dictionary
    if len(bookstore['authors']) <= author_id:
        return 'Invalid author ID!'
    return bookstore['authors'][author_id]

def add_book(bookstore, title, isbn, author_id):
    # Check if there are any books in the library to begin with
    if not 'books' in bookstore:
        return 'Invalid bookstore'
    # Put the book here
    bookstore['books'].append( {
        'title':title,
        'isbn':isbn,
        'author_id':author_id,
        'id':len(bookstore['books']) } )
    # Return the author by default
    return bookstore['books'][-1]

def get_book_by_title(bookstore, title):
    # Check if book is in by title
    for book in bookstore['books']:
        # If correct book is there return
        if book['title'] == title:
            return book
    return 'Book not found in bookstore'

def get_book_by_id(bookstore, book_id):
    if len(bookstore['books']) <= book_id:
        return 'Book not found in bookstore'
    return bookstore['books'][book_id]

def get_books_by_author(bookstore, author_id):
    output = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            output.append(book)
    return output
