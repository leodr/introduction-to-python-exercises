print("Bitte geben Sie Ihr Alter an.")

age = input("Alter: ")

age_as_number = float(age)

if 14 <= age_as_number < 18:
    print("Sie sind nach deutschem Recht Jugendlicher.")
else:
    print("Sie sind nach deutschem Recht kein Jugendlicher.")
