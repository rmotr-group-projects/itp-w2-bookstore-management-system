def create_bookstore(name):
    bookstore = {
        'name': name,
        'authors': [],
        'books' : [],
        'last_author_id' : 0,
        'last_book_id': 0
    }
    
    return bookstore
    
def add_author(bookstore, name, nationality):
	author = {
		'name' : name,
		'nationality' : nationality,
		'id' : bookstore['last_author_id']
	}
	
	bookstore['authors'].append(author)
	bookstore['last_author_id'] += 1
	return author

def get_author_by_name(bookstore, name):
	for author in bookstore['authors']:
		if author['name'] == name:
			return author

def get_author_by_id(bookstore, author_id):
	for author in bookstore['authors']:
		if author['id'] == author_id:
			return author

def add_book(bookstore, title, isbn, author_id):
    	book = {
		'title' : title,
		'isbn' : isbn, 
		'id' : bookstore['last_book_id'],
		'author_id': author_id
	}
	
	bookstore['books'].append(book)
	bookstore['last_book_id'] += 1
	return book
	
def get_book_by_title(bookstore, title):
	for book in bookstore['books']:
		if book['title'] == title:
			return book

def get_book_by_id(bookstore, book_id):
	for book in bookstore['books']:
		if book['id'] == book_id:
			return book

def get_books_by_author(bookstore, author_id):
    book_list = []
    for book in bookstore['books']:
        if book['author_id'] == author_id:
            book_list.append(book)
    return book_list



