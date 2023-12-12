"""
@Author: Divyansh Babu

@Date: 2023-12-12 22:47

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-12 22:47

@Title : Address Book System Problem.
"""
import logging

logging.basicConfig(filename='employee_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m:%d:%y''%I:%M:%S %p')
logger = logging.getLogger(__name__)


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

    def update_contact(self):
        """
        Description: This function for updating contact.
        Parameter: None.
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
                    change_company = input("Enter new first name: ")
                    self.first_name = change_company
                case 2:
                    change_company = input("Enter new last name: ")
                    self.last_name = change_company
                case 3:
                    change_company = input("Enter new address: ")
                    self.address = change_company
                case 4:
                    change_company = input("Enter new city: ")
                    self.city = change_company
                case 5:
                    change_company = input("Enter new state: ")
                    self.state = change_company
                case 6:
                    change_company = input("Enter new phone number: ")
                    self.phone = change_company
                case 7:
                    change_company = input("Enter new email address: ")
                    self.email = change_company
                case 8:
                    change_company = input("Enter new zip code: ")
                    self.pin = change_company
                case 9:
                    break


class AddressBook:
    def __init__(self, address_book_name):
        self.address_book_name = address_book_name
        self.contact_dict = {}

    def add_contact(self, contact_obj):
        """
        Description: This function for adding a contact to contact dictionary.
        Parameter: contact class object as parameter.
        Return:None
        """
        self.contact_dict.update({contact_obj.first_name: contact_obj})

    def contact_details(self):
        """
        Description: This function get all contact details from contact dictionary.
        Parameter: None
        Return:None
        """
        for key, value in self.contact_dict.items():
            print(f"first name: {key} last name: {value.last_name} phone number: {value.phone} ")

    def contact_update(self, name):
        """
        Description: This function for updating contact.
        Parameter: string
        Return:None
        """
        contact_obj: Contact = self.contact_dict.get(name)
        if contact_obj:
            contact_obj.update_contact()


def main():
    """
    Description: This function for calling all the methods in all classes.
    Parameter: None
    Return:None
    """
    address_book_name = input("Enter the book name: ")
    addressbook_obj = AddressBook(address_book_name)
    try:
        while True:
            choice = int(input("""
                        1. Add contact
                        2. get all details of contact
                        3. update conte info
                        4. exit
            """))
            match choice:
                case 1:
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
                case 2:
                    addressbook_obj.contact_details()
                case 3:
                    name = input("Enter name: ")
                    addressbook_obj.contact_update(name)
                case 4:
                    break
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()
