def create_bookstore(name):
    store = {'name': name}
    store['authors'] = {}
    store['books'] = {}
    return store


def add_author(bookstore, name, nationality):
    current_author = {'id': name, 'name': name, 'nationality': nationality}
    bookstore['authors'][name] = current_author
    return current_author
    
    
def get_author_by_name(bookstore, name):
	return bookstore['authors'][name]


def get_author_by_id(bookstore, author_id):
    return bookstore['authors'][author_id]


def add_book(bookstore, title, isbn, author_id):
    book = {'title': title, 'isbn': isbn, 'author_id': author_id, "id": title}
    bookstore['books'][title] = book
    return book


def get_book_by_title(bookstore, title):
    return bookstore['books'][title]
    

def get_book_by_id(bookstore, book_id):
    books = bookstore['books']
    for key in books:
        results = books[key]
        if book_id == results['id']:
            return results


def get_books_by_author(bookstore, author_id):
    books_list = []
    
    books = bookstore['books']
    for key in books:
        author_to_compare = books[key]['author_id']
        if author_id == author_to_compare:
            books_list.append(books[key])
        
    return books_list
        

