from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


# address_book = AddressBook()

# record1 = Record("John Doe")
# record1.add_phone(Phone("123456789"))
# record1.add_phone(Phone("987654321"))

# print(record1)

# record2 = Record("Jane Smith")
# record2.add_phone(Phone("555555555"))

# print(record2.phones)

# address_book.add_record(record1)
# address_book.add_record(record2)

# print(address_book.data)