def create_bookstore(name):
    
    return {
        'name': name,
        'books': [],
        'authors': [],
        'lastAuthorId' : 0,
        'lastBookId' : 0,
    }
#creating initial dictionary for bookstore
def add_author(bookstore, name, nationality):
    bookstore['lastAuthorId'] += 1
    newAuthor= {
        'name' : name,
        'nationality' : nationality,
        'id' : bookstore['lastAuthorId']
    }
    bookstore['authors'].append(newAuthor)
    return newAuthor
#appending newAuthor into authors list
def get_author_by_name(bookstore, name):
    for author in bookstore['authors']:
        if author['name'] == name:
            return author

# if author name entered matches authors name in list...

def get_author_by_id(bookstore, author_id):
    for author in bookstore['authors']:
        if author['id'] == author_id:
            return author

# if author id entered matches authors id in list...

def add_book(bookstore, title, isbn, author_id):
    bookstore['lastBookId'] += 1
    newBook = {
        "title" : title,
        "isbn" : isbn,
        "author_id" : author_id,
        "id" : bookstore['lastBookId']
    }
    bookstore['books'].append(newBook)
    return newBook

# appending newBook into books list

def get_book_by_title(bookstore, title):
    for book in bookstore['books']:
        if book['title'] == title:
            return book


def get_book_by_id(bookstore, book_id):
    for book in bookstore['books']:
        if book['id'] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    allAuthorBooks = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            allAuthorBooks.append(book)
            
    return allAuthorBooks
