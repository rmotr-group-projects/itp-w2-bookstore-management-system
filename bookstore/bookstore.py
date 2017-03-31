def create_bookstore(name):
    return {'name': name, 'lastauthorid': 1, 'lastbookid':1, 'books' : [], 'authors' : []}

def add_author(bookstore, name, nationality):
    newauthor = {'name': name, 'nationality': nationality, 'id': bookstore['lastauthorid']}
    bookstore['authors'].append(newauthor)
    bookstore['lastauthorid'] += 1
    return newauthor

    
def get_author_by_name(bookstore, name):
    for authors in bookstore['authors']:
        if authors['name'] == name:
            return authors

def get_author_by_id(bookstore, author_id):
    for authors in bookstore['authors']:
        if authors['id'] == author_id:
            return authors
        
        

def add_book(bookstore, title, isbn, author_id):
    newbook = {'isbn' : isbn, 'title' : title, 'author_id' : author_id, 'id' : bookstore['lastbookid']}
    bookstore['books'].append(newbook)
    bookstore['lastbookid'] += 1
    return newbook
    

def get_book_by_title(bookstore, title):
    for books in bookstore['books']:
        if books['title'] == title:
            return books


def get_book_by_id(bookstore, book_id):
    for books in bookstore['books']:
        if books['id'] == book_id:
            return books


def get_books_by_author(bookstore, author_id):
    booklist =[]
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            booklist.append(book)
    return booklist

