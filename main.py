import json
import re

is_on = True

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = {}
    with open("contacts.json", "w+") as file:
        json.dump(contacts, file)

def save():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def get_valid_name():
    while True:
        name = input("Enter name: ")
        if name:
            if name in contacts.keys():
                print("This name already exists in your phonebook. Please choose a different name.")
            else:
                return name
        else:
            print("Name cannot be empty. Please enter a valid name.")


def get_valid_phone_number():
    pattern = r'^09\d{9}$'
    while True:
        phone_number = input("Enter a Cellphone number: ")
        if bool(re.match(pattern, phone_number)):
            return phone_number
        else:
            print("Please enter a valid cellphone number.")

def get_valid_email():
    pattern = r'^[\w\.\+\-]+@[a-z\d\._\-]+\.[a-z]+$'
    while True:
        email = input("Enter email address: ")
        if bool(re.match(pattern, email)):
            return email
        else:
            print("Please enter a valid email address.")
def AddUser():
    name = get_valid_name()
    phone_number = get_valid_phone_number()
    email = get_valid_email()

    contacts[name] = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
    }
    save()

def search():
    search_name = input("Please enter contact name to search: ")

    if search_name in contacts.keys():
        print(
            f"Name: {contacts[search_name]['name']} | "
            f"Phone Number: {contacts[search_name]['phone_number']} | "
            f"Email: {contacts[search_name]['email']}"
            )
    else:
        print(f"Contact '{search_name}' not found in your phonebook.")

def edit():
    editable_contact = input("Please enter contact name to edit: ")

    if editable_contact in contacts.keys():
        new_name = get_valid_name()
        new_phone_number = get_valid_phone_number()
        new_email = get_valid_email()

        contacts[editable_contact].update({
            "name": new_name,
            "phone_number": new_phone_number,
            "email": new_email,
        })

        contacts[new_name] = contacts.pop(editable_contact)

        save()
        print(f"{editable_contact}'s information has been updated.")
    else:
        print(f"Contact '{editable_contact}' not found.")

def delete():
    delete_contact = input("Please enter contact name to delete: ")

    if delete_contact in contacts.keys():
        del contacts[delete_contact]
        print(f"{delete_contact} deleted from your phonebook.")
        save()
    else:
        print(f"Contact '{delete_contact}' not found in your phonebook.")


def show():
    for contact in contacts.keys():
        print(
            f"Name: {contacts[contact]["name"]} |"
            f"Phone Number: {contacts[contact]["phone_number"]} |"
            f"Email: {contacts[contact]["email"]}"
        )

def sort():
    sorted_contacts = dict(sorted(contacts.items(), key=lambda x: x[0]))
    print("Your contact's list sorted by name.")
    return sorted_contacts


while is_on:
    try:
        choice = int(input("""
            Please choose an option:
            1. Add new contact.
            2. Search a contact by name.
            3. Edit an exist contact.
            4. Delete a contact.
            5. View all contacts.
            6. Sort contacts.
            7. Exit.
            Enter chosen number here: """))

        if choice > 7:
            print("Please enter a number between 1 and 7")

        if choice == 7:
            is_on = False
            print("Thank You.")

        elif choice == 1:
            AddUser()

        elif choice == 2:
            search()

        elif choice == 3:
            edit()

        elif choice == 4:
            delete()

        elif choice == 5:
            show()

        elif choice == 6:
            contacts = sort()
            show()

    except ValueError:
         print("Please enter a number between 1 and 7")


