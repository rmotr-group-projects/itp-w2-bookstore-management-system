## One more:

def create_bookstore(name):
    store = {"name": name,
        "authors": {},
        "books": {}
    }

    return store

def add_author(bookstore, name, nationality):
    bookstore["authors"][name] = {}
    
    bookstore["authors"][name]["name"] = name
    bookstore["authors"][name]["nationality"] = nationality
    bookstore["authors"][name]["id"] = len(name)
    
    return bookstore["authors"][name]
    

def get_author_by_name(bookstore, name):

    return bookstore["authors"][name]


def get_author_by_id(bookstore, author_id):

    authorID = {}
    
    for nomen in bookstore["authors"]:
        item = bookstore["authors"][nomen]
        for item2 in item:
            item3 = item[item2]
            authorID[item3] = item2
            if author_id in authorID:
                return bookstore["authors"][nomen]


def add_book(bookstore, title, isbn, author_id):
    bookstore["books"][title] = {}
    
    bookstore["books"][title]["title"] = title
    bookstore["books"][title]["isbn"] = isbn
    bookstore["books"][title]["author_id"] = author_id
    bookstore["books"][title]["id"] = len(title)
    
    return bookstore["books"][title]


def get_book_by_title(bookstore, title):
    
    return bookstore["books"][title]


def get_book_by_id(bookstore, book_id):
    
    bookID = {}
    
    for liber in bookstore["books"]:
        item = bookstore["books"][liber]
        for item2 in item:
            item3 = item[item2]
            bookID[item3] = item2
            if book_id in bookID:
                return bookstore["books"][liber]


def get_books_by_author(bookstore, author_id):
    
    booksbyauthor = []

    for liber in bookstore["books"]:
        item = bookstore["books"][liber]
        if author_id in item.values():
            booksbyauthor.append(item)
            print(item)
    return booksbyauthor