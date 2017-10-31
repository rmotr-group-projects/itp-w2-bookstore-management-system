
def create_bookstore(name):
    store = {}
    store["name"]  = name
    store["authors"] = []
    store["books"] = []
    return store

def add_author(bookstore, name, nationality):
    # lowering the name + gettin the last name to use it as an ID
    name_lower = name.lower()
    name_arr = name_lower.split(" ")
    last_item_in_name_arr = len(name_arr) - 1
    author_name = name_arr[last_item_in_name_arr]
    
    our_author = {
        "name" : name,
        "nationality" : nationality,
        "id" : author_name
        }
    
    bookstore["authors"].append(our_author)
    return our_author
    
    
  
     


def get_author_by_name(bookstore, name):
    for authors in bookstore["authors"]:
        if authors["name"] == name:
            return authors
    return None


def get_author_by_id(bookstore, author_id):
    
    for authors in bookstore["authors"]:
        if author_id == authors["id"]:
            return authors
    return None
        
        


def add_book(bookstore, title, isbn, author_id): 
    new_book = {
        "title" : title,
        "isbn" : isbn,
        "author_id" : author_id,
        "id" : title + "id"
        
    }
    bookstore["books"].append(new_book)
    return new_book


def get_book_by_title(bookstore, title):
    for book in bookstore["books"]:
        if title == book["title"]:
            return book
    return None


def get_book_by_id(bookstore, book_id):
    for book in bookstore["books"]:
        if book_id == book["id"]:
            return book
    return None


def get_books_by_author(bookstore, author_id):
    book_collection = [] 
    
    for book in bookstore["books"]:
        if author_id == book["author_id"]:
            book_collection.append(book)
    return book_collection
