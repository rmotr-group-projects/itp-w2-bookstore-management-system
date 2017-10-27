dictionary = {}

def create_bookstore(name):
    dictionary['name'] = name
    dictionary['author'] = {}
    dictionary['books'] = {}
    return dictionary
    
def add_author(bookstore, name, nationality):
    name1 = dictionary['author']
    if name not in dictionary['author']:
        name1[name] = {}
        name1[name]['name'] = name
        name1[name]['nationality'] = nationality
        name1[name]['id'] = name + '1'
   # print (name1)
    return name1[name]

def get_author_by_name(bookstore, name):
    if name in dictionary['author']:
      #  print (dictionary['author'][name])
        return dictionary['author'][name]

def get_author_by_id(bookstore, author_id):
    for author in dictionary['author']:
        if dictionary['author'][author]['id'] == author_id:
      #      print (dictionary['author'][author])
            return dictionary['author'][author]
        return "Author ID Does Not Exist"

def add_book(bookstore, title, isbn, author_id):
    if title not in dictionary['books']:
        dictionary['books'][title] = {}
        dictionary['books'][title]['title'] = title
        dictionary['books'][title]['isbn'] = isbn
        dictionary['books'][title]['id'] = title + '1'
        dictionary['books'][title]['author_id'] = author_id
    #print (dictionary['books'])
    return dictionary['books'][title]

def get_book_by_title(bookstore, title):
    if title in dictionary['books']:
       # print (dictionary['books'][title])
        return dictionary['books'][title]

def get_book_by_id(bookstore, book_id):
    for book in dictionary['books']:
        if dictionary['books'][book]['id'] == book_id:
            #print (dictionary['books'][book])
            return dictionary['books'][book]
    return "Book ID Does Not Exist"

def get_books_by_author(bookstore, author_id):
    author_book_list = []
    
    for book in dictionary['books']:
        if dictionary['books'][book]['author_id'] == author_id:
            author_book_list.append(dictionary['books'][book])
    print (author_book_list)
    if author_book_list > 0:
        return author_book_list
    return "Author Has No Books"
            
'''
store = create_bookstore("rmotr's bookstore")
poe = add_author(store, 'Edgar Alan Poe', 'US')
joyce = add_author(store, 'James Joyce', 'UK')

ulysses = add_book(store, 'Ulysses', 'XXX-2', joyce['id'])

print (ulysses['title'])

print get_book_by_id(store, 'Ulysses1')
'''