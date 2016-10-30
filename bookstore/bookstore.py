def create_bookstore(name):
    bookstore = {'name' : name, 'last_author_id': 0,'last_book_id': 0,'authors': {},'books':{}}
    return bookstore


def add_author(bookstore, name, nationality):
    authorid = bookstore['last_author_id']
    bookstore['authors'].update({bookstore['last_author_id']: {'name': name, 'nationality': nationality,'id':authorid}})
    bookstore['last_author_id'] += 1
    return bookstore['authors'][authorid]


def get_author_by_name(bookstore, name):
    for items in bookstore['authors']:
        for names in bookstore['authors'][items]:
            if bookstore['authors'][items][names] == name:
                return bookstore['authors'][items]
    

def get_author_by_id(bookstore, author_id):
    for items in bookstore['authors']:
        if items == author_id:
            return bookstore['authors'][items]


def add_book(bookstore, title, isbn, author_id):
    bookid = bookstore['last_book_id']
    bookstore['books'].update({bookstore['last_book_id']: {'title': title, 'isbn': isbn,'author_id':author_id,'id': bookid}})
    bookstore['last_book_id'] += 1
    return bookstore['books'][bookid]
    

def get_book_by_title(bookstore, title):
    for items in bookstore['books']:
        for names in bookstore['books'][items]:
            if bookstore['books'][items][names] == title:
                return bookstore['books'][items]


def get_book_by_id(bookstore, book_id):
    for items in bookstore['books']:
       if items == book_id:
           return bookstore['books'][items]


def get_books_by_author(bookstore, author_id):
    list1 = []
    for items in bookstore['books']:
        if bookstore['books'][items]['author_id'] == author_id:
            list1.append(bookstore['books'][items])
    return list1
    
    