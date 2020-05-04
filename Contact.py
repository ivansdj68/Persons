class Contact:

    def __init__(self, name="", phone="", email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def askInfo(self):
        print("Enter contact info")
        self.name = input("Name: ")
        self.phone = input("Phone: ")
        self.email = input("Email: ")
        self.address = input("Address: ")

    def showInfo(self):
        print("Name: " + self.name + '\n' +
              "Phone: " + self.phone + '\n' +
              "Email: " + self.email + '\n' +
              "Address: " + self.address + '\n'
              )
