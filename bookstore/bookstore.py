from collections import defaultdict

def create_bookstore(name):
    # Create the bookstore dictionary where names, authors, and books will be stored
    bookstore = {'name': name, 'authors':[], 'books':[]}
    return bookstore

def add_author(bookstore, name, nationality):
   
   bookstore.get('authors').append({'name': name, 'nationality': nationality,'id':id(name)})
   
   return bookstore['authors'][-1]
   
def get_author_by_name(bookstore, name):
    # We store authors dict in a list in the bookstore dictionary we search for
    # 
    for author in bookstore['authors']:
        if author['name'] == name:
            return author

def get_author_by_id(bookstore, author_id):
    
            
    # We go through the dictionary filled with author information
    for author in bookstore['authors']:
                
        # When we find the matching ID we return the entire authors dictionary
        if author['id'] == author_id:
            return author

def add_book(bookstore, title, isbn, author_id):
    
    #adds the title to the bookstore dictionary
    bookstore.get('books').append({'title': title , 'isbn': isbn,'author_id': author_id, 'id': id(title)})
    
    return bookstore['books'][-1]

def get_book_by_title(bookstore, title):
    
    # for each dict in bookstore 
    for book in bookstore['books']:
        
        if book['title'] == title:

            return book

def get_book_by_id(bookstore, book_id):
    
    # for each dict in bookstore 
    for books in bookstore['books']:
        
        if books['id'] == book_id:

            return books

def get_books_by_author(bookstore, author_id):
    #sets up the final list for the two names
    all_titles = []
    
    for book in bookstore['books']:
        if book['author_id'] == author_id:
                all_titles.append(book)
                
    return all_titles

