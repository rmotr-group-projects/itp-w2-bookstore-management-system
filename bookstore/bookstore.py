#return dictionary with {'name': name}
def create_bookstore(name):
    rmotr_bookstore = {}
    rmotr_bookstore['name'] = name
    rmotr_bookstore['authors'] = {}
    rmotr_bookstore['books'] = {}
    return rmotr_bookstore
    
#return dictionary each other within the larger bookstore dict 
def add_author(bookstore, name, nationality):
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    author_id = "ID-%d" % (len(bookstore['authors']))
    author['id'] = author_id
    bookstore['authors'][author_id] = author
    return author

#return entire author dictionary accessed via that author's 'name' key
def get_author_by_name(bookstore, name):
     for auth_id in bookstore['authors']:
         if bookstore['authors'][auth_id]['name'] == name:
             return bookstore['authors'][auth_id]
    
#return entire author dictionary accessed via that author's 'author_id' key    
def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]
    
   
#return dictionary as added to ['books'] key of larger bookstore dict    
def add_book(bookstore, title, isbn, author_id):
    book = {}
    book['title'] = title
    book['isbn'] = isbn
    book['author_id'] = author_id
    id_ing = author_id + "~" + str(len(bookstore['books']))
    book_id = id_ing
    book['id'] = book_id
    bookstore['books'][book_id] = book
    return book

#return a given books dictionary accessed via that same books 'title' key
def get_book_by_title(bookstore, title):
    for bkID in bookstore['books']:
        if bookstore['books'][bkID]['title'] == title:
            return bookstore['books'][bkID]

#return a given books dictionary accessed via that same books 'id' key
def get_book_by_id(bookstore, book_id):
    return bookstore['books'][book_id]
    
    
#return a list of the book dictionaries associated with a given author_id
#Make sure each new book dict becomes the 0th index in the list    
def get_books_by_author(bookstore, author_id):
    authors_books = []
    for bkID in bookstore['books']:
        if bookstore['books'][bkID]['author_id'] == author_id:
            book_log = {'title': bookstore['books'][bkID]['title'],
            'isbn': bookstore['books'][bkID]['isbn'],
            'author_id': bookstore['books'][bkID]['author_id']}
            authors_books = [book_log] + authors_books
            
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
