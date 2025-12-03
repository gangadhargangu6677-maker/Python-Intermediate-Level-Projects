import json
import os

def load_contacts():
    if not os.path.exists("contacts.json"):
        return []
    with open("contacts.json", "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def show_menu():
    print("\nContact Book")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts = load_contacts()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        if not contacts:
            print("No contacts found")
        else:
            print("\nSaved Contacts:")
            for c in contacts:
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts(contacts)

        print("Contact added")

    elif choice == "3":
        keyword = input("Enter name or phone to search: ").lower()
        found = False

        for c in contacts:
            if keyword in c["name"].lower() or keyword in c["phone"]:
                print(f"Found Contact -> Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                found = True

        if not found:
            print("No matching contact found")

    elif choice == "4":
        delete_name = input("Enter name of contact to delete: ").lower()
        updated_list = [c for c in contacts if c["name"].lower() != delete_name]

        if len(updated_list) != len(contacts):
            contacts = updated_list
            save_contacts(contacts)
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
