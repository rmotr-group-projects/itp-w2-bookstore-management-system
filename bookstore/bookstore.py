id_list = []  # list of unique ID's

# added function to generate a unique ID using random integers; saves to global list
def autoGen():
    import random
    gen = random.randint(0,10000000)
    if gen not in id_list:
        id_list.append(gen)
        return gen

def create_bookstore(name):
    bookstore = {}
    bookstore['name'] = name
    bookstore['books'] = {}
    bookstore['authors'] = {}
    return bookstore

def add_author(bookstore, name, nationality):
    author = {}
    author['name'] = name
    author['nationality'] = nationality
    uniqueID = autoGen()
    author['id'] =  uniqueID
    bookstore['authors'][uniqueID] = author
    return author

def add_book(bookstore, title, isbn, author_id):
    book = {}
    book['title'] = title
    book['isbn'] = isbn
    book['author_id'] = author_id
    uniqueID = autoGen()
    book['id'] = uniqueID
    bookstore['books'][uniqueID] = book
    return book

def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]

def get_book_by_id(bookstore, book_id):
    return bookstore['books'][book_id]

def get_author_by_name(bookstore, name):
    smallerDict = bookstore['authors']
    for key in smallerDict.keys():
        if smallerDict[key]['name'] == name:
            return smallerDict[key]

def get_book_by_title(bookstore, title):
    smallerDict = bookstore['books']
    for key in smallerDict.keys():
        if smallerDict[key]['title'] == title:
            return smallerDict[key]

def get_books_by_author(bookstore, author_id):
    set_of_books = []
    smallerDict = bookstore['books']
    for key in smallerDict.keys():
        if smallerDict[key]['author_id'] == author_id:
            set_of_books.append(smallerDict[key])
    return set_of_books
