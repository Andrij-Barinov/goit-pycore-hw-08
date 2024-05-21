from utils import input_error
from models import AddressBook, Record

@input_error
def add_contact(args, book):
    # Adds a new contact or updates an existing one
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    # Change the phone number in a contact
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, book):
    # Shows phone numbers for the specified contact
    name = args[0]
    record = book.find(name)
    if record:
        return ', '.join(phone.value for phone in record.phones)
    else:
        return "Contact not found."

@input_error
def add_birthday(args, book):
    # Adds a birthday to a contact
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book):
    # Shows the contact's birthday
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")
    elif record:
        return "Birthday not set."
    else:
        return "Contact not found."

def birthdays(args, book):
    # Shows birthdays that will take place within the next week
    upcoming = book.get_upcoming_birthdays(7)
    return "\n".join(str(record) for record in upcoming)

def show_all(book):
    # Shows all contacts
    return "\n".join(str(record) for record in book.data.values())