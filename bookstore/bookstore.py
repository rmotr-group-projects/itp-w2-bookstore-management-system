#return dictionary with {'name': name}
def create_bookstore(name):
    rmotr_bookstore = {'name': name, 'authors': [], 'books': []}
    return rmotr_bookstore

#return dictionary for each author within the larger bookstore dict
def add_author(bookstore, name, nationality):
    author_id = len(bookstore['authors'])
    author = {'name': name, 'nationality': nationality, 'id': author_id}
    bookstore['authors'].append(author)
    return author

#return entire author dictionary accessed via that author's 'name' key
def get_author_by_name(bookstore, name):
     for auth_id in bookstore['authors']:
         if auth_id['name'] == name:
             return auth_id

#return entire author dictionary accessed via that author's 'author_id' key
def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]


#return dictionary as added to ['books'] key of larger bookstore dict
def add_book(bookstore, title, isbn, author_id):
    book_id = str(author_id) + '-' + str(len(bookstore['books']))
    book = {'title': title, 'isbn': isbn, 'author_id': author_id, 'id': book_id}
    bookstore['books'].append(book)
    return book
    
"""
def add_author(bookstore, name, nationality):
    author_id = len(bookstore['authors'])
    author = {'name': name, 'nationality': nationality, 'id': author_id}
    bookstore['authors'].append(author)
    return author
    """

#return a given books dictionary accessed via that same books 'title' key
def get_book_by_title(bookstore, title):
    for bkID in bookstore['books']:
        if bkID['title'] == title:
            return bkID

def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book
            
        


#return a list of the book dictionaries associated with a given author_id
def get_books_by_author(bookstore, author_id):
    authors_books = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            authors_books.append(book)
    return authors_books


#TEST INPUTS
#store = create_bookstore("rmotr's bookstore")   
#poe = add_author(store, 'Edgar Allan Poe', 'US')
#borges = add_author(store, 'Jorge Luis Borges', 'AR')
#joyce = add_author(store, 'James Joyce', 'UK')

#raven = add_book(store, 'The Raven', 'XXX-1', poe['id'])
#ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])
#ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
#aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])

#print get_books_by_author(store, borges['id'])


#FEDE's ID_GENERATOR CODE

#writers_id_list = [0] #Global list that stores writers id

#def writers_id_generator(): 
 #   id = 0
  #  id = max(writers_id_list) + 1
   # writers_id_list.append(id)
    #return id
    
#books_id_list = [0] #Global list that stores books id

#def books_id_generator(): 
 #   id = 0
  #  id = max(books_id_list) + 1
   # books_id_list.append(id)
    #return id
