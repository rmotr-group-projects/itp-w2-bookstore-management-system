def create_bookstore(name):
    # Create the bookstore dictionary where names, authors, and books will be stored
    bookstore = {}
    
    # Create a key 'name' where the bookstore name will be stored
    bookstore['name'] = name
    # return bookstore to user
    return bookstore

def add_author(bookstore, name, nationality):
    # Adding the author to the bookstore dictionary
    bookstore[name] = {'name': name, 'nationality': nationality,'id':hash(name)}
    
    # Returning dictionary which contains the authors information
    return bookstore[name]


def get_author_by_name(bookstore, name):
    # We store authors by name in the dictionary we search for
    # the key matching the name
    for key in bookstore.keys():
        if key == name:
            
            # Return the dictionary with all the authors information
            return bookstore[key]


def get_author_by_id(bookstore, author_id):
    
    # First we go through the bookstore dictionary
    for bookstore_key in bookstore.keys():
        
        # If the value is a dictionary we continue
        if type(bookstore[bookstore_key]) is dict:
            
            # We go through the dictionary filled with author inforamtion
            for author_key in bookstore[bookstore_key].keys():
                
                # When we find the matching ID we return the entire authors dictionary
                if bookstore[bookstore_key][author_key] == author_id:
                    return bookstore[bookstore_key]


def add_book(bookstore, title, isbn, author_id):
    pass


def get_book_by_title(bookstore, title):
    pass


def get_book_by_id(bookstore, book_id):
    pass


def get_books_by_author(bookstore, author_id):
    pass
