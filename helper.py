
import json
# display menu, get user selection
def menu():
    print("2 - add")
    print("3 - print")
    print("4 - delete")
    print("5 - search")
    print("6 - exit")
    user_selection=input("your selection:")
    return int(user_selection)

# load from file to list contacts
def load(DATA_FILE):
    
    # try:
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
    # except:pass

# save contacts list to a file
def save(DATA_FILE,contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f)


""" add a new contact to contacts list"""
def add(contacts): contacts.append({"name":input("your name?"),"cell":input("cell")})
   
# print all contacts
def print_all(contacts): print(contacts)


# search by name...
def search(contacts):
    contact_2_search=input("su esmak?")

    for contact in contacts:
        if contact['name'] == contact_2_search:
            print (f"found, name: {contact['name']} cell: {contact['cell']}")
            return #exit the function
    print(f"not found {contact_2_search}")

def delete(data):
    contact_2_search=input("su esmak?")
    for contact in data:
        if contact["name"] == contact_2_search:
            print (f"delete, name: {contact['name']} cell: {contact['cell']}")
            data.remove(contact)
            return
    print(f"not found {contact_2_search}")
