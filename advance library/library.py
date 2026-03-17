from storage import load_books, save_books

def add_book(title):
    books = load_books()
    books.append(title)
    save_books(books)
    print("Book added")
def view_books():
    for b in books():
        print(b)
def remove_book(title):
    books = load_books()
    if title in books:
        books.remove(title)
        save_books(books)
        print("Book removed")
    else:
        print("Book not found. cannot able to remove")