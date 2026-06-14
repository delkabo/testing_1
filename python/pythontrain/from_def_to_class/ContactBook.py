
class ContactBook:
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email
        })

    def find_contact(self, name):
        get_contact=[]
        for contact in self.contacts:
            if contact['name'] == name:
                return contact
            # if contact['name'] == name:
            #     get_contact.append(contact)
            #     # return contact
            # if len(get_contact) != 0:
            #     return get_contact
        return None

    def update_contact(self, name, new_phone=None, new_email=None):
        contact = self.find_contact(name)
        if contact:
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            return True
        return False


# Использование

MyContactBook = ContactBook()
MyContactBook.add_contact('Иван', '+79101234567', 'ivan@mail.com')
MyContactBook.update_contact('Иван', '+79101231111', 'ivan@yandex.com')
# MyContactBook.add_contact('Мария', '+79107654321', 'maria@mail.com')
print("!!!!!", MyContactBook.find_contact('Иван'))
# print("!!!!!", MyContactBook.find_contact('Мария'))

# add_contact('Иван', '+79101234567', 'ivan@mail.com')
# add_contact('Мария', '+79107654321', 'maria@mail.com')
# print(find_contact('Иван'))