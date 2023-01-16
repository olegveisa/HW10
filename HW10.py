from collections import UserDict

class Field():
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.value = phone

class Record():
    def __init__(self, name: Name, *phones):
        self.name = name
        self.phones = list(phones)

    def add_phone(self, value: Phone):
        self.phones.append(value)
    
    def change_phone(self, old_phone: Phone, new_phone: Phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)

    def delete_phone(self, phone: Phone):
        self.phones.remove(phone)

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record
        
if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')