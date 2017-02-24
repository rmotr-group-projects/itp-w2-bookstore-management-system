def create_bookstore(name):
    KCM_bookstore = {'name':name, 'authors':{}, 'books':{}}
    return KCM_bookstore

def add_author(bookstore, name, nationality):
    author_id = len(bookstore['authors'])
    author = {'name':name, 'nationality':nationality, 'id':author_id}
    bookstore['authors'][author_id] = author
    return author
    
def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if name == bookstore['authors'][author]['name']:
            return bookstore['authors'][author]

def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]


def add_book(bookstore, title, isbn, author_id):
    book_id = len(bookstore['books'])
    book = {'title':title, 'isbn':isbn, 'author_id':author_id, 'id':book_id}
    bookstore['books'][book_id] = book
    return book

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if title == bookstore['books'][book]['title']:
            return bookstore['books'][book]


def get_book_by_id(bookstore, book_id):
    return bookstore['books'][book_id]


def get_books_by_author(bookstore, author_id):
    result = []
    for book in bookstore['books']:
        if author_id == bookstore['books'][book]['author_id']:
            result.append(bookstore['books'][book])
    return result


KCM_bookstore = create_bookstore('KCM_bookstore')
kyle = add_author(KCM_bookstore, 'kyle', 'US')
Manny = add_author(KCM_bookstore, 'Manny', 'US')
Cyn = add_author(KCM_bookstore, 'Cyn', 'US')
Harry_Potter = add_book(KCM_bookstore, 'Harry Potter', 123, kyle['id'])
lord_of_the_rings = add_book(KCM_bookstore, 'Lord of the Rings', 456, Manny['id'])
star_wars = add_book(KCM_bookstore, 'Star Wars', 789, Manny['id'])
print(KCM_bookstore)
print(get_author_by_name(KCM_bookstore, "Manny"))
print(get_author_by_id(KCM_bookstore, 0))
print(get_book_by_title(KCM_bookstore, 'Harry Potter'))
print(get_book_by_title(KCM_bookstore, 'Lord of the Rings'))
print(get_book_by_id(KCM_bookstore, 0))
print(KCM_bookstore['books'])
print(KCM_bookstore['authors'])
print(get_books_by_author(KCM_bookstore, Manny['id']))