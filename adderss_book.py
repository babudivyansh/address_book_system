"""
@Author: Divyansh Babu

@Date: 2023-12-12 14:27

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-12 14:27

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


# class AddressBook:
#     def __init__(self, address_book_name):
#         self.address_book_name = address_book_name
#         self.contact_dict = {}
#
#     def add_contact(self, contact_obj):
#         self.contact_dict.update({contact_obj.first_name: contact_obj})


def main():
    """
        Description: This function for calling all the methods in all classes.
        Parameter: None
        Return:None
    """
    # address_book_name = input("Enter the book name: ")
    # addressbook_obj = AddressBook(address_book_name)
    while True:
        print("choice 1 to add contact")
        choice = int(input("Enter your choice: "))
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
                                        "city": city,
                                        "state": state, "pin": pin, "phone": phone, "email": email}
                contact_obj = Contact(contact_detalis_dict)
                # addressbook_obj.add_contact(contact_obj)
            case 2:
                break


if __name__ == '__main__':
    main()
