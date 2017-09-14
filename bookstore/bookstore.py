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
    for bookstore_value in bookstore.values():
        
        # If the value is a dictionary we continue
        if type(bookstore_value) is dict:
            
            # We go through the dictionary filled with author information
            for author_key in bookstore_value.keys():
                
                # When we find the matching ID we return the entire authors dictionary
                if bookstore_value[author_key] == author_id:
                    return bookstore_value


def add_book(bookstore, title, isbn, author_id):
    
    #adds the title to the bookstore dictionary
    bookstore[title] = {'title': title , 'isbn': isbn,'author_id': author_id, 'id': id(title)}
    return bookstore[title]

def get_book_by_title(bookstore, title):
    
    # for each dict in bookstore 
    for book_titles in bookstore.keys():
        
        if book_titles == title:

            return bookstore[book_titles]

def get_book_by_id(bookstore, book_id):
    
    for book_titles in bookstore.values():
       
       if type(book_titles) is dict:
           
          for book_data in book_titles.keys():
              
              if book_titles[book_data] == book_id:
                  return book_titles
              
            

def get_books_by_author(bookstore, author_id):
    all_titles = []
    for book_titles in bookstore.values():
       
       if type(book_titles) is dict and 'nationality' not in book_titles:
          
          for book_data in book_titles.keys():
              
            if book_titles[book_data] == author_id:
                all_titles.append(book_titles)
    return all_titles