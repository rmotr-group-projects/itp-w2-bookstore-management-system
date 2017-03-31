def create_bookstore(name):
    store_dict = {  "name" : name,
                    "author" : [],
                    "book" : []
    }
    return store_dict
    
def add_author(bookstore, name, nationality):
    auth_id = len(name)*len(nationality)
    author_dict = {  "id" : auth_id,  
                     "name" : name, 
                     "nationality" : nationality
    } 
    bookstore["author"].append(author_dict)
    return author_dict

def get_author_by_name(bookstore, name):
    for author in bookstore["author"]:
        if author['name'] == name:
            return author

def get_author_by_id(bookstore, author_id):
    for author in bookstore["author"]:
        if author["id"] == author_id:
            return author

# store_dict ===> author: [{'name': 'Poe', 'nationality': 'US', 'id':4354}, {'name': 'Poe', 'nationality': 'US', 'id':4354}, {'name': 'Poe', 'nationality': 'US', 'id':4354},{'name': 'Poe', 'nationality': 'US', 'id':4354}  ]
# for i in bookstore["author"]:
#     i['name'] == 'Poe'
#     if i['id'] == author_id

def add_book(bookstore, title, isbn, author_id):
    book_id = len(title)*int(isbn[4]) 
    book_dict = {   "title" : title,
                    "isbn" : isbn,
                    "author_id" : author_id,
                    "id" : book_id
    }
    bookstore["book"].append(book_dict)
    return book_dict

def get_book_by_title(bookstore, title):
    for book in bookstore["book"]:
        if book["title"] == title:
            return book

def get_book_by_id(bookstore, book_id):
    for book in bookstore["book"]:
        if book["id"] == book_id:
            return book


def get_books_by_author(bookstore, author_id):
    auth_books = []
    for books in bookstore["book"]:
        if books["author_id"] == author_id:
            auth_books.append(books)
    return auth_books
