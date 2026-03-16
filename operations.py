from phonebook import phonebook

def add_contact():
    name = input("Enter name:")
    number = input("Enter number:")

    phonebook[name] = number
    print("Contact Added Successfully")

def search_contact():
    name = input("Enter name to search:")

def delete_contact():
    name = input("Enter name to delete:")

    if name in phonebook:
        del phonebook[name]
        print("Contact deleted")
    else:
        print("Contact not found")
def update_contact():
    name = input("Enter name to update")

    if name in phonebook:
        new_number = input("Enter new number:")
        phonebook[name] = new_number

def display_contact():
    if len(phonebook) == 0:
        print("Phonebook id empty")
    else:
        print("\n phonebook contacts: ")

        for name, number in phonebook.items():
            print(name, ":",number)