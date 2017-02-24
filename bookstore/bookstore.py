def create_bookstore(name):
    rmotr_bookstore = {}
    rmotr_bookstore['name'] = name
    rmotr_bookstore['authors'] = {}
    rmotr_bookstore['books'] = {}
    return rmotr_bookstore
    
 
def add_author(bookstore, name, nationality):
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    author_id = "ID-%d" % (len(bookstore['authors']))
    author['id'] = author_id
    bookstore['authors'][author_id] = author
    return author
    
    
"""#store = create_bookstore("rmotr's bookstore")    
#poe = add_author(store, 'Edgar Allan Poe', 'US')
#print(poe)

    
    
#store = create_bookstore("my_store")
#poe = add_author(bookstore, 'Edgar Allan Poe', 'US')
#print add_author("store" , "Edgar Allan Poe", "US")
    
    

#store = create_bookstore("bookstore")
#poe = add_author("bookstore", "Edgar Allan Poe", "US")    

#bookstore[writers_id]['id'] = writers_id"""

    
    
def get_author_by_name(bookstore, name):
     for auth_id in bookstore['authors']:
         if bookstore['authors'][auth_id]['name'] == name:
             return bookstore['authors'][auth_id]
    
    
def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]
    
   
    
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
    
def get_book_by_title(bookstore, title):
    for bkID in bookstore['books']:
        if bookstore['books'][bkID]['title'] == title:
            return bookstore['books'][bkID]


def get_book_by_id(bookstore, book_id):
    return bookstore['books'][book_id]
    
    
    
def get_books_by_author(bookstore, author_id):
    authors_books = []
    for bkID in bookstore['books']:
        if bookstore['books'][bkID]['author_id'] == author_id:
            book_log = {'title': bookstore['books'][bkID]['title'],
            'isbn': bookstore['books'][bkID]['isbn'],
            'author_id': bookstore['books'][bkID]['author_id']}
            authors_books = [book_log] + authors_books
            
    return authors_books
            

"""store = create_bookstore("rmotr's bookstore")   
poe = add_author(store, 'Edgar Allan Poe', 'US')
borges = add_author(store, 'Jorge Luis Borges', 'AR')
joyce = add_author(store, 'James Joyce', 'UK')

raven = add_book(store, 'The Raven', 'XXX-1', poe['id'])
ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])
ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])
    
print get_books_by_author(store, borges['id'])"""


    


"""
store = create_bookstore("rmotr's bookstore")    

borges = add_author(store, 'Jorge Luis Borges', 'AR')

ficciones = add_book(store, 'Ficciones', 'XXX-3', borges['id'])
aleph = add_book(store, 'El Aleph', 'XXX-4', borges['id'])

print(get_books_by_author("rmotr's bookstore", borges['id']))
"""


""""
writers_id_list = [0] #Global list that stores writers id

def writers_id_generator(): 
    id = 0
    id = max(writers_id_list) + 1
    writers_id_list.append(id)
    return id
    
books_id_list = [0] #Global list that stores books id

def books_id_generator(): 
    id = 0
    id = max(books_id_list) + 1
    books_id_list.append(id)
    return id
"""