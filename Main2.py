# arr = [1,2,2,3,4,4,5]
# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)
    

# distict = set(arr)
# print(distinct)

# {1:1,2:2,3:1,4:2,5:1}

# {1,2,3,4,5}

# # duplicate values
# arr = [1,1,2,2,3,4,5]
# depulicate = {}

# for num in arr:
#      depulicate[num] = depulicate.get(num, 0) + 1
# for key, value in depulicate.items():
#     if value > 1:
#         print(key)
   

# arr = [1,2,3,4,5]

# seen = set()

# duplicate = False
# for num in arr:
#     if num in seen:
#         duplicate = True
#         break
#     seen.add(num)

# if duplicate:
#     print("Duplicates present")
# else:
#     print("No duplicates")

# Library project



library = {}

def add_book():
    book = input("Enter book name:")
    author = input("Enter author name:")
    library[book] = author
    print("Book added successfully!")
def view_books():
    if len(library) == 0:
        print("Library empty")
    else:
        for book in library:
            print(book, "y", library[book])

def search_book():
    book = input("Enter book name to search:")
    if book in library:
        print("Aouther: ", library[book])
    else:
        print("Book not found")


def delete_book():
    book = input("book not found")

    if book in library:
        del library[book]
        print("Book deleted successfully")
    else:
        print("Book not found")

def main():
    while True:
        print("1. Add book")
        print("2. View books")
        print("3. Search book")
        print("4. Delete book")
        print("5. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

main()