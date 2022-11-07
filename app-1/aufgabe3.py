print("Wie lautet der Vorname des Erfinders von Python?")

print("(G)uido")
print("(T)homas")
print("(P)eter")

antwort = input("Antwort: ")

if antwort.lower() == "g":
    print("Richtig!")
else:
    print("Falsch.")

print("")
print("")
print("Zu welchem Datentyp gehört dieses Literal: 12.0")

print("(i)nt")
print("(f)loat")
print("(s)tr")

antwort = input("Antwort: ")

if antwort.lower() == "f":
    print("Richtig!")
else:
    print("Falsch.")
