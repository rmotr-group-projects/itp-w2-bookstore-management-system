def create_bookstore(name):
    library = {'name': name,
                'authors': {},
                'books' : {},
                'author_id': 1
    }

    return library

def add_author(bookstore, name, nationality):
    author = name
    bookstore['authors'][author] = {'name' : name, 
                                    'nationality' : nationality,
                                    'id' : bookstore['author_id']
    }
    bookstore['author_id'] += 1
    return bookstore['authors'][author]

# str(name[:3]) + nationality

def get_author_by_name(bookstore, name):
    for key in bookstore['authors']:
        if key == name:
            continue 
        
    return bookstore['authors'][name]

def get_author_by_id(bookstore, author_id):
    for key, values in bookstore['authors'].items():
        if values['id'] == author_id:
            return values

def add_book(bookstore, title, isbn, author_id):
    bookstore['books'][title] = {'title': title,
                        'isbn' : isbn,
                        'author_id' : author_id,
                        'id' : str(title[:3]) + isbn
                        
    }
    return bookstore['books'][title]


def get_book_by_title(bookstore, title):
    return bookstore['books'][title]


def get_book_by_id(bookstore, book_id):
    for key, values in bookstore['books'].items(): 
        if values['id'] == book_id:    
            return values


def get_books_by_author(bookstore, author_id):
    booklist = []
    for book in bookstore['books'].values():
        if book['author_id'] == author_id:
            booklist.append(book)
    return booklist