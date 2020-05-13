# TODO Alternative create contact class for storing and reading contact info
# TODO Create class that stores, search, and removes contacts
class AddressBook:
    def __init__(self):
        # Default fields in address book
        self.fields = ['Name', 'Phone', 'Email', 'Address']
        # TODO Add CSV import to address_book and contact_list
        self.address_book = {
            'Juan Pablo Del Pueblo': {
                self.fields[0]: 'Juan Pablo Del Pueblo',
                self.fields[1]: '787-777-9999',
                self.fields[2]: 'juanPablo@coqui.net',
                self.fields[3]: 'Calle Jurutungo, Utuado, PR, 00759'
            },
            'Maria Magdalena del Pilar': {
                self.fields[0]: 'Maria Magdalena del Pilar',
                self.fields[1]: '787-787-9999',
                self.fields[2]: 'maria@coqui.net',
                self.fields[3]: 'Calle Calle, Vieques, PR, 00000'
            },
            'Juan Pedro Del Pueblo': {
                self.fields[0]: 'Juan Pedro Del Pueblo',
                self.fields[1]: '787-797-9999',
                self.fields[2]: 'juanPedro@coqui.net',
                self.fields[3]: 'Calle Jurutungo, Utuado, PR, 00759'
            }
        }
        self.contact_list = []

    def add_contact(self, contact_info):
        """Adds contact info for each field available from contact_info array obtained in
        the InfoWindow. Once added, it updates the address book with new contact."""
        # Generate key for dictionary
        keyword = contact_info[0]
        # Create a nested dictionary where keyword is key, and each field is a sub-key
        info = dict(zip(self.fields, contact_info))
        contact = {keyword: info}
        # Update dictionary
        self.address_book.update(contact)

    def deleteContact(self, key):
        """Method that deletes a contact from a keyword selected from GUI"""
        del self.address_book[key]

    # new_contact_info can be an array with the following content:
    # new_contact_info = [old_name, new_name, new_phone, new_email, new_address]
    def editContact(self, new_contact_info):
        current_contact_info = self.address_book.get(new_contact_info[0])
        current_contact_info["Name"] = new_contact_info[1]
        current_contact_info["Phone"] = new_contact_info[2]
        current_contact_info["Email"] = new_contact_info[3]
        current_contact_info["Address"] = new_contact_info[4]
        del self.address_book[new_contact_info[0]]
        self.address_book.update({new_contact_info[1]: current_contact_info})

    #TODO Add method for editing contact info
    def editContact(self, key, newinfo):
        found = self.address_book.get(key)
        #TODO Add returning every key back to entry/input so as to be modified
        #TODO Add updating any changes done by user
        #Update key to newest name
        keyword = found['Name']
        if key == keyword:
            self.address_book[key] = found
        else:
            self.address_book[keyword] = self.address_book.pop(key)
            self.address_book[keyword] = found

    def sortList(self):
        return self.contact_list.sort()

    def searchList(self, contact_name):
        if self.isNameInAddressBook(contact_name):
            return self.address_book[contact_name]  # Returns sub-dictionary with contact_name's info
        else:
            print("Invalid search criteria or contact does not exist")

    def isNameInAddressBook(self, contact_name):
        return contact_name in self.address_book  # Returns true if contact_name is a key in address_book

    def get_address_book_names(self):
        names = []
        for name in self.address_book:
            names.append(name)
        return names

# # For Testing purposes
# address = AddressBook()
#
# # Test Adding
# add = True
# while add:
#     address.add_contact()
#     repeat = input('Do you wish to continue? ')
#     add = repeat.lower() in ['yes', 'y']
#
# # Test Search
# address.searchList()
