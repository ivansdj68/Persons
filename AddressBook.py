import json
import os.path

class AddressBook:
    def __init__(self):
       """Constructor that will initialize Address Book from a JSON file, 
        if file is not found it will create a new JSON file"""
       
       self.address_book ={}

       if os.path.isfile('contacts.json'):
           with open('contacts.json') as json_file:
               data = json.load(json_file)

           self.address_book = data 
       else:
           open ('contacts.json','x')

       self.contact_list= []


    def add_contact(self, contact_info):
        """Adds contact info for each field available from contact_info dictionary obtained in
        the InfoWindow. Once added, it updates the address book with new contact. Saves changes to 
        a JSON file"""
        # Generate key for dictionary
        keyword = contact_info["Name"]
        # Create a nested dictionary where keyword is key, and each field is a sub-key
        contact = {keyword: contact_info}
        # Update dictionary
        self.address_book.update(contact)
        self.save_json()

    def edit_contact(self,keyname,contact_info):
        """ Receives contact name and edited information. If the name of contact has changed it
        will move old values to new contact name. Regardless of outcome it will update the information
        from the new information. Saves at the end to a JSON file."""

        new_keyname = contact_info["Name"]
        if keyname != new_keyname:
            self.address_book[new_keyname] = self.address_book.pop(keyname)
        
        for k, v in self.address_book.items():
            self.address_book[new_keyname][k] = v
        
        self.save_json()

    def delete_contact(self, key):
        """Method that deletes a contact from a keyword selected from GUI"""
        del self.address_book[key]
        self.save_json()

    def sort_list(self):
        if self.sorted:
            self.contact_list.sort(reverse=False)
            self.sorted = False
        else:
            self.contact_list.sort(reverse=True)
            self.sorted = True
        return self.contact_list

    def search_list(self, contact_name):
        """ Returns sub-dictionary with contact_name's info """
        return self.address_book[contact_name] 

    def contact_exists(self, contact_name):
        """ Returns true if contact_name is a key in address_book """
        return contact_name in self.address_book  

    def get_names(self):
        for name in self.address_book:
            self.contact_list.append(name)
        self.contact_list.sort()
        self.sorted = False
        return self.contact_list

    def save_json(self):
        with open('contacts.json','w') as outfile:
            json.dump(self.address_book,outfile,sort_keys=True, indent= 4)