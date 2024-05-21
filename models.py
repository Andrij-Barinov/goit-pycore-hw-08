from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        # Initializing a field with a passed value
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Class for storing a contact name
    pass

class Phone(Field):
    # Class for storing a phone number with validation
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    # Class for storing the date of birth with validation
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    # Class for storing a contact record
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        # Add a phone number to the record
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Delete a phone number from the record
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Change the phone number in the record
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def add_birthday(self, birthday):
        # Add a birthday to a record
        self.birthday = Birthday(birthday)

    def __str__(self):
        # Return a string representation of a record
        phones = ', '.join(str(phone) for phone in self.phones)
        birthday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "No birthday"
        return f"{self.name.value}: {phones}, Birthday: {birthday}"

class AddressBook(UserDict):
    # Class for storing an address book
    def add_record(self, record):
        # Add an entry to the address book
        self.data[record.name.value] = record

    def find(self, name):
        # Find a record by name
        return self.data.get(name)

    def delete(self, name):
        # Delete a record by name
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days):
        # Return the list of records with birthdays for the next week
        today = datetime.today()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year)
                if today <= next_birthday <= today + timedelta(days=days):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays