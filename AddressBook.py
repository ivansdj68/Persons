from Contact import *

class AddressBook:

    def __init__(self, book=[]):
        self.book = book
        self.size = len(book)

    def getSize(self):
        return self.size

    def addContact(self, contact):
        self.book.append(contact)
        self.size += 1
        #self.book.sort(key=contact.getName())

    def deleteContact(self, contact):
        self.book.remove(contact)
        self.size -= 1

    def editContact(self, contact):
        index = self.book.index(contact)
        contact.askInfo()
        self.book.insert(index, contact)

    def getContact(self, info):
        if info[0].isdigit():
            no_dashes = info.replace('-', '')
            return self.getContactByPhone(no_dashes)
        elif info[0].isalpha():
            if info.find('@') >= 0:
                return self.getContactByEmail(info)
            else:
                return self.getContactByName(info)

    def getContactByName(self, contact_name):
        for c in range(len(self.book)):
            current_contact = self.book[c]
            if current_contact.getName() == contact_name:
                return current_contact
        return None

    def getContactByPhone(self, phone):
        for c in range(len(self.book)):
            current_contact = self.book[c]
            if current_contact.getPhone() == phone:
                return current_contact
        return None

    def getContactByEmail(self, email):
        for c in range(len(self.book)):
            current_contact = self.book[c]
            if current_contact.getEmail() == email:
                return current_contact
        return None

    def getContactByIndex(self, index):
        return self.book[index]

    def showAddressBook(self):
        for c in range(len(self.book)):
            self.book[c].showInfo()

    def showContact(self, contact):
        for c in range(len(self.book)):
            current = self.book[c]
            if current.getName() == contact:
                current.showInfo()
