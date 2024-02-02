
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact has already been added"
    
    else:
        contacts[name] = phone
        return "Contact added."


def change_phone(args, contacts):
    name, phone = args
    if name not in contacts:
        return "There are no contact with this name"
    else:
        contacts[name] = phone

    return "Contact changed"


def show_phone(args, contacts):
    name, *_ = args
    result = contacts.get(name)
    return f"{name} has phone {result}"


def delete_phone(args, contacts):
    name, *_ = args
    del contacts[name]

    return "Contact deleted"


def clear_contacts(contacts):

    contacts.clear()
    return "Contacts clear"


def show_all(contacts):
    if not contacts:
        return "Contacts is empty"
    return f"Contacts: {contacts}"
