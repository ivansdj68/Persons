#TODO Alternative create contact class for storing and reading contact info
#TODO Create class that stores, search, and removes contacts
class AddressBook:
    def __init__(self):
        #Default fields in address book
        self.fields = ['Name','Phone','Email','Address','City','State','Zip Code']
        #TODO Add CSV import to address_book and contact_list
        self.address_book = {
            'Me':{
                self.fields[0]:'Juan Del Pueblo',
                self.fields[1]:'787-777-9999',
                self.fields[2]:'juan@coqui.net',
                self.fields[3]:'Calle Jurutungo',
                self.fields[4]:'Utuado',
                self.fields[5]:'PR',
                self.fields[6]:'00759'
            }

        }
        self.contact_list = []

    
    def add_contact(self):
       """Adds contact info for each field available from input/entry from user. Once added it updates
       the address book with new contact"""
       fields = self.fields
       values = []
       #TODO Add ability to add new field if needed
       #TODO Change loop inputs to entries from GUI
       for field in fields:
           value = input(field + ': ')
           values.append(value)

       #Generate key for dictionary
       keyword = values[0]

       #Create a nested dictionary where keyword is key, and each field is a subkey
       info = dict(zip(fields,values))
       contact = {keyword:info}

       #Update dictionary
       self.address_book.update(contact)

    def deleteContact(self,key):
        """Method that deletes a contact from a keyword selected from GUI"""
        del self.address_book[key]



    #TODO Add method for searching for contact info

    #TODO Add method for editing contact info
    def editContact (self,key):
        pass


    #TODO Add a sorted list of contacts
    def sortList(self):
        return self.contact_list.sort()

    #TODO Alternative search from a list once selected
    def searchList(self):
        for key in self.address_book:
            self.contact_list.append(key)
        search = input('Enter Name: ') #TODO Subtitute with entry box
        result = [i for i in self.address_book if search in i]
        #TODO Substitute for-print with a return list to addressGUI
        for name in sorted(result):
            print(name)

#For Testing purposes
address = AddressBook()

#Test Adding
add = True
while add:
    address.add_contact()
    repeat = input('Do you wish to continue? ')
    add = repeat.lower() in ['yes','y']

#Test Search
address.searchList()

