from input_error import input_error
from entities import AddressBook, Field, Name, Phone, Record

def hello_handler():
    return "How can I help you?"

def close_handler():
    return "Good bye!"

@input_error
def add_handler(contact):

    name, phone = contact.split(' ')
    record = Record(name)
    record.add_phone(Phone(phone))
    address_book.add_record(record)
    print(address_book)
    # phonebook[name] = phone
    return "Contact added successfully"

@input_error
def change_handler(contact):
    name, phone = contact.split(' ')
    phonebook[name] = phone
    return "Phone number changed successfully"

@input_error
def phone_handler(name):
    return phonebook[name]

def show_all_handler():
    if not address_book:
        return "No contacts found"
    contacts = []
    for name, phone in address_book.data:
        contacts.append(f"{name}: {phone}")
    return (address_book)


def main():

    

    while True:
        
        request = input().lower()


        if request == "good bye" or request == "close" or request == "exit":
            print(close_handler())
            break

        elif request == "hello":
            print(hello_handler())

        elif request == 'show all':
            print(show_all_handler())
        
        elif request.split(' ')[0] == 'add':
            result = add_handler(request[4:])
            print(result)

        elif request.split(' ')[0] == 'change':
            result = change_handler(request[7:])
            print(result)

        elif request.split(' ')[0] == 'phone':
            number = phone_handler(request[6:])
            print(number)

        else:
            print('I do not understand you')

        



if __name__ == '__main__':
    address_book = AddressBook()
    main()
