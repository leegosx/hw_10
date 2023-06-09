from collections import UserDict
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

class Record:
    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = []
            self.phones.append(phone)

class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
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
