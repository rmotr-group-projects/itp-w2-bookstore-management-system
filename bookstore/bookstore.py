def create_bookstore(name):
    return {
        "name": name,
        "authors": [],
        "books": []
    }


def get_bookstore_name(bookstore):
    return bookstore["name"]


def add_author(bookstore, name, nationality):
    author = {
        "name": name,
        "nationality": nationality
    }
    bookstore["authors"].append(author)
    return author


def get_author_by_name(bookstore, name):
    for author in bookstore["authors"]:
        if name.lower() == author["name"].lower():
            return author


def add_book(bookstore, title, isbn, author):
    book = {
        "title": title,
        "isbn": isbn,
        "author": author
    }
    bookstore["books"].append(book)
    return book


def get_book_by_title(bookstore, title):
    for book in bookstore["books"]:
        if title.lower() == book["title"].lower():
            return book


def get_books_by_author(bookstore, author):
    books = []
    for book in bookstore["books"]:
        if author.lower() == book["author"].lower():
            books.append(book)
    return books
