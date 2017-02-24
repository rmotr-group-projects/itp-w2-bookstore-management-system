# store = {'name': "rmotr's bookstore",
#     'authors': {
#         'poe': {'name': 'Edgar Allan Poe', 'nationality': 'US', 'id': 15}, 
#         'borges': {'name': 'Jorge Luis Borges', 'nationality': 'AR', 'id': 17}, 
#         'joyce': {'name': 'James Joyce', 'nationality': 'UK', 'id': 11}}, 
#     'books': {'The Raven': {'title': 'The Raven', 'isbn': 'XXX-1', 'author id': 15}, 
#       'Ulysses': {'title': 'Ulysses', 'isbn': 'XXX-2', 'author id': 11}, 
#       'Ficciones': {'title': 'Ficciones', 'isbn': 'XXX-3', 'author id': 17}, 
#       'El Aleph': {'title': 'El Aleph', 'isbn': 'XXX-4', 'author id': 17}}}


# raven = {'title': 'The Raven', 'isbn': 'XXX-1', 'author': 'Edgar Allan Poe'}
# ulysses = {'title': 'Ulysses', 'isbn': 'XXX-2', 'author': 'James Joyce'}
# ficciones = {'title': 'Ficciones', 'isbn': 'XXX-3', 'author': 'Jorge Luis Borges'}
# aleph = {'title': 'El Aleph', 'isbn': 'XXX-4', 'author': 'Jorge Luis Borges'}



def create_bookstore(name):
    store = {"name": name,
        "authors": {},
        "books": {}
    }

    return store

def add_author(bookstore, name, nationality):
    bookstore["authors"][name] = {}
    
    bookstore["authors"][name]["name"] = name
    bookstore["authors"][name]["nationality"] = nationality
    bookstore["authors"][name]["id"] = len(name)
    
    return bookstore["authors"][name]
    

def get_author_by_name(bookstore, name):

    return bookstore["authors"][name]


def get_author_by_id(bookstore, author_id):

    authorID = {}
    
    for nomen in bookstore["authors"]:
        item = bookstore["authors"][nomen]
        for item2 in item:
            item3 = item[item2]
            authorID[item3] = item2
            if author_id in authorID:
                return bookstore["authors"][nomen]


def add_book(bookstore, title, isbn, author_id):
    bookstore["books"][title] = {}
    
    bookstore["books"][title]["title"] = title
    bookstore["books"][title]["isbn"] = isbn
    bookstore["books"][title]["author id"] = author_id
    bookstore["books"][title]["book id"] = len(ti)
    
    return bookstore["books"][title]


def get_book_by_title(bookstore, title):
    
    return bookstore["books"][title]


def get_book_by_id(bookstore, book_id):
    
    bookID = {}
    
    for liber in bookstore["books"]:
        item = bookstore["books"][liber]
        for item2 in item:
            item3 = item[item2]
            bookID[item3] = item2
            if book_id in bookID:
                return bookstore["books"][liber]


def get_books_by_author(bookstore, author_id): # for this function you are supposed to return a list of dictionary objects for each book that has the author_id passed
    
    authorID = {}
    booksbyauthor = []
    
    for liber in bookstore["books"]:
        item = bookstore["books"][liber]
        for item2 in item:
            item3 = item[item2]
            authorID[item3] = item2
            if author_id in authorID:
                booksbyauthor.append(item)
                return booksbyauthor


"""
>>> for key, value in store['authors'].items():
	print(key, value)

	
joyce {'id': 11, 'nationality': 'UK', 'name': 'James Joyce'}
borges {'id': 17, 'nationality': 'AR', 'name': 'Jorge Luis Borges'}
poe {'id': 15, 'nationality': 'US', 'name': 'Edgar Allan Poe'}


>>> for key, value in store['authors'].items():
	if value['id'] == 11:
		print('joyce')
	else:
		print('not found')

		
joyce
not found
not found
>>> 
"""