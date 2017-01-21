import time

def create_bookstore(name):
    
    return {

        'name' : name, 
        'authors' : []
    }

def add_author(bookstore, name, nationality):
    
    ln = len(bookstore['authors'])
    author = {

        'name' : name, 
        'nationality' : nationality, 
        'id' : len(bookstore['authors']), 
        'books' : []
    }

    bookstore['authors'].append(author)
    return bookstore['authors'][ln]


def get_author_by_name(bookstore, name):
    
    for i in bookstore['authors'] : 
        if i['name'] == name : 
            return i


def get_author_by_id(bookstore, author_id):
    
    for i in bookstore['authors'] : 
        if i['id'] == author_id : 
            return i
        else : 
            pass

def add_book(bookstore, title, isbn, author_id):
    
    book = {

        'title' : title, 
        'isbn' : isbn, 
        'book_id' : time.time()
    }

    for i in bookstore['authors'] : 
        if i['id'] == author_id : 
            i['books'].append(book)
            
    return book


def get_book_by_title(bookstore, title):
    for i in bookstore['authors'] : 
        for j in range(len(i['books'])) : 
            if i['books'][j]['title'] == title : 
                return i['books'][j]
            else : 
                pass


def get_book_by_id(bookstore, book_id):
    
    for i in bookstore['authors'] : 
        for j in range(len(i['books'])) : 
            if i['books'][j]['book_id'] == book_id : 
                return i['books'][j]
            else : 
                pass

def get_books_by_author(bookstore, author_id):
    
    for i in bookstore['authors'] : 
        if i['id'] == author_id : 
            return i['books']
        else : 
            pass