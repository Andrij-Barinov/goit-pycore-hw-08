import pickle
from models import AddressBook

def save_data(book, filename="addressbook.pkl"):
    # Saves address book state to a file
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    # Loads the address book state from a file if the file exists, otherwise creates a new book
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Return a new address book if the file is not found

def parse_input(user_input):
    # The function splits the entered string into a command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    # Decorator for handling exceptions that may occur in command functions
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner