from collections import UserDict
from datetime import datetime, timedelta

def input_error(func):
    def inner(phones, birthday):
        try:
            func(phones, birthday)
        except IndexError:
            print("Please enter norm number")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("plese, press norm number or date birthday")
    return inner

class AdressBook(UserDict):
    # count = 1

    def __init__(self):
        super().__init__(self)
        self.max_value = 1
        self.current_value = 0
        self.page = 1
        self.page_size = 1
        
    def add_record(self, record):
        for i in record.phones:
            if isinstance(i, Phone) and i.value.startswith('+') and len(i.value) == 13:
                self.data[record.name.value] = record
            else:
                raise ValueError("plese, press norm number")

    def __iter__(self):
        self.page = 1
        return self

    def __next__(self):
        start = (self.page - 1) * self.page_size
        end = start_index + self.page_size
        records = list(self.data.values())[start:end]
        if not records:
            raise StopIteration
        self.page += 1
        for rec in records:
            print(rec.name.value, rec.phones)
        return self

    

class Record:
    def __init__(self, name, *phones, birthday=None):
        self.name = name
        self.phones = list(phones)
        self.birthday = birthday
        if phone:
            self.phones.append(phone)
                
    
    @input_error
    def days_to_birthday(self): 
        date_now = datetime.now()
        self.birthday = datetime.strptime(self.birthday, '%d-%m-%Y')
        self.birthday = self.birthday.replace(year=date_now.year)
        date_days = self.birthday - datetime.now()
        return date_days.days

    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
        

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = Phone(new_phone)
 
    def get_phones(self):
        return [phone.get_value() for phone in self.phones]

# здесь логика добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
    

class Field:
    def __init__(self, value):
        self.value = value
    
# который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.

class Name(Field):
    pass

class Phone(Field):
    pass

if __name__ == "__main__":
    name = Name('bob')
    phone = Phone('+123456789000')
    rec = Record(name, phone)
    ab = AdressBook()
    ab.add_record(rec)
    assert isinstance(ab['bob'], Record)
    assert isinstance(ab['bob'].name, Name)
    assert isinstance(ab['bob'].phones, list)
    assert isinstance(ab['bob'].phones[0], Phone)
    assert ab['bob'].phones[0].value == '+123456789000'
    print('All Ok)')

