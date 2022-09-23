application_name = 'ListNer'

# Welcome
print(f'{application_name} | Welcome')

new_list = []
default_value = 0
new_item = default_value

print(new_list)


# Add item to new_list
def add_item(list_name, item):
    list_name.append(item)


# Remove item from new_list
def remove_item(list_name, item_index):
    list_name.remove(item_index)


# Using a while loop to allow the user to exit the application when they want instead of it closing on its own
while True:
    add_or_remove = str.lower(input("(Add) to add items \n(Remove) to remove items\n(Exit) to exit application: "))

    if add_or_remove == "add":
        while True:
            new_item = input("What item would you like to add? Enter: ")
            if not new_item.isdigit():
                add_item(new_list, new_item)
                print("Successfully added...")
                break
    elif add_or_remove == "remove":
        while True:
            new_item = input("Which item you would like to remove? Enter: ")
            if new_item in new_list:
                remove_item(new_list, new_item)
                print("Successfully removed...")
                break
            elif new_item not in new_list:
                print("Invalid arguments...\nPlease check the capital letters and spelling...")
                break
    elif add_or_remove == "exit":
        print("Ending process...")
        quit()
    else:
        print("Invalid arguments...\nPlease try again...")

    # Printing the list to show the changes done to it
    print(new_list)
    # Reset new_item value
    new_item = default_value

# I don't know what I just wrote
# But it works
# So I am happy
# :)