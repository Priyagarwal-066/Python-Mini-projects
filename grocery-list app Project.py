grocery_list = []
while True:
        print("Options: add/remove/show/exit")
        action = input("What would you like to do?")
        if action == "add":
            item = input("Enter item to add:")
            grocery_list.append(item)
            print(f"{item} added.")
        elif action == "remove":
            item = input("Enter item to remove:")
            if item in grocery_list:
                grocery_list.remove(item)
                print(f"{item} removed.")
            else:
                print("item not found.")
        elif action == "show":
            print("Your grocery list:")
            for i in grocery_list:
                print("-",i)
        elif action == "exit":
            print("Thanks for visiting!")
            break
        else:
            print("invalid option.")



