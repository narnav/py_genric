"""
method list
 menu
# load
# add
# print
# delete
# search
"""


from  helper import *
contacts=[]
DATA_FILE='my_contacts.json'
# implemented

def main():
    contacts=load(DATA_FILE) # load from file to contacts list
    user_selection= menu() # get user selection from menu 
    while  user_selection != 6:
        if user_selection == 2:add(contacts) # add new contact to contacts
        if user_selection == 3:print_all(contacts) #print all contacts
        if user_selection == 4:delete(contacts) # delete a contact
        if user_selection == 5:search(contacts) # search a contact
        user_selection= menu()
    save(DATA_FILE,contacts) # save all contacts to JSON file

if __name__ == "__main__":
    main()