data = []


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def create():
    print("")
    print("Neuen Kontakt erstellen.")

    name = input("Name   : ")
    number = input("Nummer : ")
    data.append(Contact(name, number))

    print(f"{name} wurde hinzugefügt.")
    print("")


def read():
    print("")
    print("Kontakte werden ausgegeben.")
    print("")

    for contact in data:
        print(f"Name   : {contact.name}")
        print(f"Nummer : {contact.number}")
        print("")


def delete():
    print("")
    print("Kontakt löschen.")

    name = input("Name der zu löschenden Person : ")

    delete_index = -1

    for index, contact in enumerate(data):
        if contact.name == name:
            delete_index = index

    if delete_index >= 0:
        del data[delete_index]
        print(f"{name} wurde gelöscht.")
        print("")
    else:
        print(f"{name} wurde nicht gefunden.")
        print("")


print("")
print("ADRESSBUCH V0.0.1")
print("")

while True:
    op = input(
        "Möchten sie (e)rstellen, (a)nzeigen, (l)öschen oder (b)eenden? :  ").lower().strip()

    if op == "e" or op == "erstellen":
        create()
    elif op == "a" or op == "anzeigen":
        read()
    elif op == "l" or op == "löschen":
        delete()
    elif op == "b" or op == "beenden":
        exit()
