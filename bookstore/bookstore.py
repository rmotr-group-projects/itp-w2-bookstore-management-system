## One more:

def create_bookstore(name):
    store = {"name": name,
        "authors": {},
        "books": []
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

    book = { "title": title, 
        "isbn": isbn,
        "author_id": author_id,
        "id": int(isbn[-1])
    }

    bookstore["books"].append(book)
    
    return book


def get_book_by_title(bookstore, title):
    
    for liber in bookstore["books"]:
        if title in liber.values():
            return liber


def get_book_by_id(bookstore, book_id):
    
    for liber in bookstore["books"]:
        if book_id in liber.values():
            return liber


def get_books_by_author(bookstore, author_id):

    booksbyauthor = []

    for liber in bookstore["books"]:
        if author_id in liber.values():
            booksbyauthor.append(liber)
    return booksbyauthor