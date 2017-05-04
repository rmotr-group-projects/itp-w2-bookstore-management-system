from collections import OrderedDict

author_id_generator = 1000
book_id_generator = 2000

def create_bookstore(name):
    if isinstance(name, str):
    	bookstore = {
    		"name" : name,
    		"authors": {},
    		"books": {}
    	}
    	return bookstore
    else:
    	"Invalid entry. Accepted input will be a string"

def add_author(bookstore, name, nationality):
    global author_id_generator
    bookstore["authors"][name] = {
    	"name" : name,
    	"nationality": nationality,
    	"id": author_id_generator
    	}
    author_id_generator += 1
    return bookstore["authors"][name]


def get_author_by_name(bookstore, name):
    if name in bookstore["authors"]:
    	return bookstore["authors"][name]
    else:
    	return "author not found"



def get_author_by_id(bookstore, author_id):
    for key, value in bookstore['authors'].items():
        if value['id'] == author_id:
            return value
        else:
            pass
        return "Author ID not found"


def add_book(bookstore, title, isbn, author_id):
    global book_id_generator
    bookstore["books"][title] = {
    "title": title,
    "isbn": isbn,
    "author_id": author_id,
    "id": book_id_generator
    }
    book_id_generator += 1
    return bookstore['books'][title]


def get_book_by_title(bookstore, title):
    if title in bookstore['books']:
    	return bookstore['books'][title]
    else:
    	return title + " not found!"


def get_book_by_id(bookstore, book_id):
    for key, value in bookstore['books'].items():
    	if book_id == value['id']:
    		return value
    	else:
    		pass
    return "book ID not found."

def get_books_by_author(bookstore, author_id):
    books_by_author = []
    for key, value in bookstore['books'].items():
        if author_id == value['author_id']:
            books_by_author.append(value)
        else:
            pass
    if len(books_by_author) > 0:
        return books_by_author
    else:
        return "No books by that author found!"