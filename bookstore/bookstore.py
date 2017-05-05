def create_bookstore(name):
    return {"name": name,
            "last_author_id" : 0,
            "last_book_id" : 0,
            "authors" : [],
            "books" : []
            }

def add_author(bookstore, name, nationality):
    bookstore["last_author_id"] += 1
    author_name = {"id" : bookstore["last_author_id"],     
         "name" : name,
         "nationality" : nationality,
         }
    bookstore["authors"].append(author_name)
    return author_name
    
    
def get_author_by_name(bookstore, name):
    for author_list in bookstore["authors"]:
        if author_list["name"] == name:
            return author_list
            


def get_author_by_id(bookstore, author_id):
    for author_list in bookstore["authors"]:
        if author_list["id"] == author_id:
            return author_list    


def add_book(bookstore, title, isbn, author_id):
    bookstore["last_book_id"] += 1
    book_name = {"id" : bookstore["last_book_id"],
                 "title" : title,
                 "isbn" : isbn,
                 "author_id" : author_id,
                 }
    bookstore["books"].append(book_name)
    return book_name

def get_book_by_title(bookstore, title):
    for book_list in bookstore["books"]:
        if book_list["title"] == title:
            return book_list


def get_book_by_id(bookstore, book_id):
    for book_list in bookstore["books"]:
        if book_list["id"] == book_id:
            return book_list
            


def get_books_by_author(bookstore, author_id):
    book_list = []
    for book in bookstore["books"]:
        if book["author_id"] == author_id:
            book_list.append(book)
    return book_list        
