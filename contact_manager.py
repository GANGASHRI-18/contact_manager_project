# contact_manager.py

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']}\n")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully\n")


def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"], "\n")
    else:
        print("Contact not found\n")


def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact updated\n")
    else:
        print("Contact not found\n")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted\n")
    else:
        print("Contact not found\n")


def main():
    contacts = load_contacts()

    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")


main()
