"""
Here are the levels:

BOOKSTORE:
-Has 3 items;
---name: This gives the name of the store
---books: This is a seperate dictionary. It contains all the books
---authors: This is a seperate dictionary. It contains all the authors

BOOKS:
-Has many items, keys are integers (0, 1, 2, 3, ...) 
--Each index (lets say bookstore['books'][0] ) is a dictionary on its own
--Each index has these values:
----Title: title of book
----ISBN: the code of book, used by librarians (just some data)
----Book id: index used to reach the book (the above case would be 0)
----Authod_id: The id number of the author

AUTHOR
-Has many items, keys are integers (0, 1, 2, 3, ...) 
--Each index (lets say bookstore['authors'][1] ) is a dictionary on its own
--Each index has these values:
----Name: name of author
----Nationality: where the author is from
----Author_id: The id number of the author (the above case would be 1)
"""

def create_bookstore(name):
    return {'name':name, 'authors':{}, 'books':{}}

def add_author(bookstore, name, nationality):
    # Check if there are any authors in the library to begin with
    if not 'authors' in bookstore:
        return 'Invalid bookstore'

    # Generate a non-existing ID
    i = 0
    while i in bookstore['authors']:
        i += 1
    
    # Put the author here
    bookstore['authors'][i] = {'name':name, 'nationality':nationality, 'id':i}
    
    # Return the author by default
    return bookstore['authors'][i]


def get_author_by_name(bookstore, name):
    
    # Check authors available
    for i in bookstore['authors']:
        # If the correct author is there, return that author
        if bookstore['authors'][i]['name'] == name:
            return bookstore['authors'][i]
    
    # If not found, return the bust string
    return 'Author not in bookstore'


def get_author_by_id(bookstore, author_id):
    
    if not author_id in bookstore['authors']:
        return 'Invalid author ID!'
    return bookstore['authors'][author_id]


def add_book(bookstore, title, isbn, author_id):
    # return {'bookstore': bookstore, 'title':title, 'isbn':isbn, 'author_id': author_id}
    
    # Check if there are any books in the library to begin with
    if not 'books' in bookstore:
        return 'Invalid bookstore'

    # Generate a non-existing ID
    i = 0
    while i in bookstore['books']:
        i += 1
    
    # Put the author here
    bookstore['books'][i] = {'bookstore': bookstore, 'title':title, 'isbn':isbn, 'author_id': author_id}
    
    # Return the author by default
    return bookstore['books'][i]


def get_book_by_title(bookstore, title):
    # Check if book is in by title
    for i in bookstore['books']:
        # If correct book is there return
        if bookstore['books'][i]['title'] == title:
            return bookstore['books'][i]
    return 'Book not found in bookstore'




def get_book_by_id(bookstore, book_id):
    if not book_id in bookstore['books']:
        return 'Invalid book ID!'
    return bookstore['books'][book_id]


def get_books_by_author(bookstore, author_id):
    if not author_id in bookstore['authors']:
        return 'Invalid author ID!'
    return bookstore['books'][author_id]
"""    
store = create_bookstore("rmotr's bookstore")

poe = add_author(store, 'Edgar Alan Poe', 'US')
borges = add_author(store, 'Jorge Luis Borges', 'AR')
joyce = add_author(store, 'James Joyce', 'UK')

raven = add_book(store, 'The Raven', 'XXX-1', poe['id'])
ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])
ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])

print (store)
"""