class ContactList(list):
    def search(self, name):
        """
        Return all contacts that contain the search value in
        their name
        :param name: string, string to compare against
        :return: list of matching contacts
        """
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class MailSender(object):
    """
    Mixin class for sending emails to contacts
    """
    def send_mail(self, message):
        """
        function printing message to terminal
        should be replaced with an http call for email but I'm lazy
        :param message: string, message to email to contact
        :return: should be http response, but...
        """
        print("sending mail to {}, with message of {}".format(self.email, message))
        # Add email logic here


class LongNameDict(dict):
    """
    Return int of longest key in dictionary
    """
    def longest_key(self):
        """
        function for finding longest key in dictionary
        :return: int, length of longest key in dictionary
        """
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


class Contact(object):
    """
    Class to store basic contact's values
    """
    all_contacts = []

    def __init__(self, name, email):
        """
        Initializes the Contact class with the contact's name,
        and email
        :param name: string, name of contact
        :param email: string, email of contact
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class EmailableContact(Contact, MailSender):
    pass


class AddressHolder(object):
    """
    object to store address values
    """
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class Supplier(Contact):
    """
    Behaves like a contact class, but has an additional
    order method
    """

    def order(self, order):
        print("If this were a real system we would send "
              "'{}' order to '{}'".format(order, self.name))
