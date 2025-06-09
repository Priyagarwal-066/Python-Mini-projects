contacts = {}
while True:

    print("options:Add Contact/View all/Search/Delete/Exit")
    action = input("Enter Option:")
    if action == "Add Contact":
        Name = input("Name:")
        Phone = int(input("Phone:"))
        print("Choose:\n1.Save\n2.Edit")
        choice = input("Enter Choice:")
        if choice == "Save":
            contacts[Name] = Phone
            print("Contact saved successfully!")
        else:
            Name = input("Name:")
            Phone = int(input("Phone:"))
            input("choice:")
            contacts[Name] = Phone
            print("Contact saved successfully!")

    elif action == "View all":
        for Name, Phone in contacts.items():
            print(f"{Name} : {Phone}")


    elif action == "Search":
        Name = input("Enter Name to search:")
        if Name in contacts:
            print(f"{Name} : {contacts[Name]}")
        else:
            print("Contact not found.")

    elif action == "Delete":
        Name = input("Enter Name to delete:")
        if Name in contacts:
            print("message : Do you really want to delete contact? \n1.Yes\n2.No")
            select = input("select:")
            if select == "Yes":
                del contacts[Name]
                print("Contact deleted successfully!" )
            else:
                print(contacts)
        else:
            print("Contact not found!")

    elif action == "Exit":
        print("Thanks for visiting!")
        break

    else:
        print("Invalid choice!")










