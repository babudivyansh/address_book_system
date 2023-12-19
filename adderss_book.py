"""
@Author: Divyansh Babu

@Date: 2023-12-19 11:29

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-19 11:29

@Title : Address Book System Problem.
"""
import csv
import logging
import sys

logging.basicConfig(filename='address_book_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m:%d:%y' '%I:%M:%S %p')
logger = logging.getLogger(__name__)

streamhdlr = logging.StreamHandler(sys.stderr)
logger.addHandler(streamhdlr)
streamhdlr.setLevel(logging.DEBUG)


class Contact:
    def __init__(self, contact_detalis_dict):
        self.first_name = contact_detalis_dict.get("first_name")
        self.last_name = contact_detalis_dict.get("last_name")
        self.address = contact_detalis_dict.get("address")
        self.city = contact_detalis_dict.get("city")
        self.state = contact_detalis_dict.get("state")
        self.pin = contact_detalis_dict.get("pin")
        self.phone = contact_detalis_dict.get("phone")
        self.email = contact_detalis_dict.get("email")
        self.file = "file_text.txt"

    def display_contact(self):
        """
        Description: This function for display all contact by city name or state name.
        Parameter: self object as parameter.
        Return:None
        """
        print(f"""
                first name: {self.first_name} 
                last name: {self.last_name} 
                phone number: {self.phone}
                address : {self.address}
                city : {self.city}
                state : {self.state}
                email : {self.email}
                Zip code : {self.pin}
        """)
        print("---------------------------------------------------------")

    def update_contact(self):
        """
        Description: This function for updating contact.
        Parameter: self object as parameter.
        Return:None
        """
        while True:
            choice = int(input("""
                        1. change first name
                        2. change last name
                        3. change address
                        4. change city
                        5. change state
                        6. change phone number
                        7. change email
                        8. change Zip code
                        9. exit
            """))
            match choice:
                case 1:
                    change_contact = input("Enter new first name: ")
                    self.first_name = change_contact
                case 2:
                    change_contact = input("Enter new last name: ")
                    self.last_name = change_contact
                case 3:
                    change_contact = input("Enter new address: ")
                    self.address = change_contact
                case 4:
                    change_contact = input("Enter new city: ")
                    self.city = change_contact
                case 5:
                    change_contact = input("Enter new state: ")
                    self.state = change_contact
                case 6:
                    change_contact = input("Enter new phone number: ")
                    self.phone = change_contact
                case 7:
                    change_contact = input("Enter new email address: ")
                    self.email = change_contact
                case 8:
                    change_contact = input("Enter new zip code: ")
                    self.pin = change_contact
                case 9:
                    break

    def add_contact_file(self):
        """
        Description: This function return all the contact info.
        Parameter: self object as parameter.
        Return:contact information.
        """
        return [f'{self.first_name} | {self.last_name} | {self.address} | {self.city} | {self.state} | {self.pin} | '
                f'{self.phone} | {self.email}']

    def add_contact_csv(self):
        return {"first_name": self.first_name, "last_name": self.last_name,
                "address": self.address, "city": self.city, "state": self.state,
                "pin": self.pin, "phone": self.phone, "email": self.email}

    def add_address_book_file(self):
        """
        Description: This function write contact data in a text file.
        Parameter: self object as parameter.
        Return:None
        """
        with open(self.file, 'a', newline="") as f:
            f.write(str(f"{self.add_contact_file()}\n"))

    def __repr__(self):
        return self.first_name


class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.csv_file = 'csv_file.csv'
        self.contact_dict = {}
        self.csv_contact_dict = {}

    def add_contact(self, contact_obj):
        """
        Description: This function for adding a contact to contact dictionary.
        Parameter: self object as parameter.
                   contact class object as parameter.
        Return:None
        """
        if contact_obj.first_name not in self.contact_dict:
            self.contact_dict.update({contact_obj.first_name: contact_obj})

        else:
            raise Exception("Contact all. present")

    def contact_details(self):
        """
        Description: This function get all contact details from contact dictionary.
        Parameter: self object as parameter.
        Return:None
        """
        for key, value in self.contact_dict.items():
            print(f"""
                    first name: {key} 
                    last name: {value.last_name} 
                    phone number: {value.phone}
                    address : {value.address}
                    city : {value.city}
                    state : {value.state}
                    email : {value.email}
                    Zip code : {value.pin}
            """)

    def contact_update(self, name):
        """
        Description: This function for updating contact.
        Parameter: string and self object as parameter.
        Return:None
        """
        contact_obj: Contact = self.contact_dict.get(name)
        if contact_obj:
            contact_obj.update_contact()
        else:
            print("contact not present!!")

    def delete_contact(self, name):
        """
        Description: This function for delete a contact.
        Parameter: string and self object as parameter.
        Return:None
        """
        if name in self.contact_dict:
            self.contact_dict.pop(name)
        else:
            print("contact not found!!")

    def display_person_in_city_or_state(self, city):
        """
        Description: This function is displaying aal the contact info using city and state .
        Parameter: string and self object as parameter.
        Return: None
        """
        contacts = dict(filter(lambda x: x[1].city.lower() == city.lower() or x[1].state.lower() == city.lower(),
                               self.contact_dict.items()))
        for i in contacts.values():
            i.display_contact()
        return len(contacts)

    def sort_data(self):
        """
        Description: This function is sorting the contact using person name.
        Parameter: self object as parameter.
        Return: None
        """
        for key, value in sorted(self.contact_dict.items()):
            value.display_contact()

    def sort_contact_using_city_state_zip(self, name):
        """
        Description: This function is sorting the contact using city, state, zip.
        Parameter: string and self object as parameter.
        Return: None
        """
        sorted_contact = sorted(self.contact_dict.values(), key=lambda x: x.city == name, reverse=True)
        for i in sorted_contact:
            i: Contact
            print(i.first_name, '>>>>', i.city)

    def write_csv(self):
        """
        Description: This function is write data in csv file.
        Parameter: self object as parameter.
        Return: None
        """
        with open(self.csv_file, 'w', newline="") as file:
            field_names = ['address_book_name', 'first_name', 'last_name', 'address', 'city', 'state', 'pin', 'phone',
                           'email']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for key, value in self.contact_dict.items():
                data = value.add_contact_csv()
                data.update({'address_book_name': key})
                writer.writerow(data)

    def read_csv(self):
        """
        Description: This function is read data from csv file.
        Parameter: self object as parameter.
        Return: None
        """
        with open(self.csv_file, mode='r') as file:
            csv_file = csv.reader(file)
            for i in csv_file:
                print(i)
            file.close()


class MultipleAddressBook:

    def __init__(self):
        self.book_dict = {}

    def add_multiple_book(self, addressbook_obj):
        """
        Description: This function add multiple book.
        Parameter: self object as parameter.
                   address book object as parameter
        Return:None
        """
        self.book_dict.update({addressbook_obj.address_book_name: addressbook_obj})

    def get_book(self, name):
        """
        Description: This function for getting the name of address book from address book dictionary .
        Parameter: string and self object as parameter.
        Return:name of address book present in address book dictionary.
        """
        return self.book_dict.get(name)


def main():
    """
    Description: This function for calling all the methods in all classes.
    Parameter: None
    Return:None
    """
    multiple_book_obj = MultipleAddressBook()
    try:
        while True:
            choice = int(input("""
                        1. Add contact
                        2. get all details of contact
                        3. update contact info
                        4. delete contact
                        5. display all contact by city or state
                        6. sort the contact
                        7. sort contact using city, state or zip
                        8. add address book file
                        9. exit
            """))
            match choice:
                case 1:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    if addressbook_obj is None:
                        addressbook_obj = AddressBook(address_book_name)
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    address = input("Enter Address: ")
                    city = input("Enter City: ")
                    state = input("Enter State: ")
                    pin = int(input("Enter Pin: "))
                    phone = int(input("Enter Phone: "))
                    email = input("Enter Email: ")
                    contact_detalis_dict = {"first_name": first_name, "last_name": last_name, "address": address,
                                            "city": city, "state": state, "pin": pin, "phone": phone, "email": email}
                    contact_obj = Contact(contact_detalis_dict)
                    addressbook_obj.add_contact(contact_obj)
                    multiple_book_obj.add_multiple_book(addressbook_obj)
                    contact_obj.add_address_book_file()
                case 2:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    addressbook_obj.contact_details()
                case 3:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter name of contact: ")
                    addressbook_obj.contact_update(name)
                case 4:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter name: ")
                    addressbook_obj.delete_contact(name)
                case 5:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter city or state name: ")
                    print(addressbook_obj.display_person_in_city_or_state(name))
                case 6:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    addressbook_obj.sort_data()
                case 7:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    name = input("Enter city or state or pin name: ")
                    addressbook_obj.sort_contact_using_city_state_zip(name)
                case 8:
                    address_book_name = input("Enter the book name: ")
                    addressbook_obj = multiple_book_obj.get_book(address_book_name)
                    addressbook_obj.write_csv()
                    addressbook_obj.read_csv()
                case 9:
                    break

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()
