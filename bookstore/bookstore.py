
def create_bookstore(name):
    bookstore = {
        'name' : name,
        'authors' : [],
        'books' : [],
        'id' : 0,
        'book_id' : 0,
        'last_function_book_list' : []
    }
    return bookstore
'''
#'id':0, <- setting up some the id in the first function that is called so it does not get reset everytime add_author is called
        #'bookid':0 <- doing the same thing for a book id as the author id
        #'last_function_book_list':[] <-- this is for the last function when we need to return the books from one author(in the test for this they add 2 books by 1 author and test that we return there are 2 books by that author)
'''

def add_author(bookstore, name, nationality):
    bookstore['id'] += 1
    author = {
        'name' : name,
        'nationality' : nationality,
        'id' : bookstore['id']
    }
    bookstore['authors'].append(author)
    return author

def get_author_by_name(bookstore, name):
    for author in bookstore['authors']: 
        if author['name'] == name:
            return author  
    
def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:  
        if author['id'] == author_id: 
            return author

def add_book(bookstore, title, isbn, author_id):
    bookstore['book_id']+=1 
    book = {
        'title': title,
        'isbn': isbn,
        'author_id' : author_id,
        'id':bookstore['book_id'] 
    }
    bookstore['books'].append(book) 
    return book
"""
#-----------------------------------------------------------    
def add_book(bookstore, title, isbn, author_id):
    #bookstore['book_id']+=1 we are doing the same thing like we did when we added an author, we are setting up the bookid variable to hold to value of bookid and then incrementing it when the function to add book is called
    book = {
        'title': title,
        'isbn': isbn,
        'id': author_id  #this is saying id is = author_id  be carefull when doing get_book_by_id you DO NOT want to call this id! It is not the book_id, it is the author_id.
        #'book_id':bookstore['book_id'], <- assigning a book_id from bookstore['bookid'](we set it up in create_dictionary so it can hold the value and all we have to do is increment it each time this function is called)
    }
    if book['title'] not in bookstore['books']: #<- like i said you really dont need this as they are not asking you to make sure there are no duplicates and the test is not trying to input multiple of the same books anywy
        bookstore['books'].append(book) 
    return book
#-----------------------------------------------------------
"""

def get_book_by_title(bookstore, title):
    for book in bookstore['books']: 
        if book['title'] == title:  
            return book
            
def get_book_by_id(bookstore, book_id):    
    for book in bookstore['books']:    
        if book['id'] == book_id:   
            return book

def get_books_by_author(bookstore, author_id):
    for book in bookstore['books']:
        if author_id==book['author_id']:
            bookstore['last_function_book_list'].append(book)
    return bookstore['last_function_book_list']

'''
def get_books_by_author(bookstore, author_id):
    return [len(get_book_by_id(bookstore, author_id))] #<- got rid of bookbyid list, 
    #for book in bookstore['books']:
        #if author_id==book['id']:
            #bookstore['last_function_book_list'].append(book)
    #return bookstore['last_function_book_list']
'''
        
