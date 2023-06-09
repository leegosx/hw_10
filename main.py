from collections import UserDict

class AddressBook(UserDict):
    def __getitem__(self, key):
        return self.data[key]
    
    def address_book(self, value):
        return value in self.data.values()
    
class Record:
    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = []
            self.phones.append(phone)
    
class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone():
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("380990658131", "380990658131")
    rec = Record(name, phone)
    ab = AddressBook()
    ab["Bill"] = rec
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab["Bill"].phones[0].phone == "380990658131"
    print("All okay")