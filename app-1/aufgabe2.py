die_sonne_strahlt = True
hohe_luftfeuchtigkeit = False
regen = True
wind = False

if die_sonne_strahlt:
    if hohe_luftfeuchtigkeit:
        print("Kein Sport.")
    else:
        print("Sport!")
else:
    if regen:
        if wind:
            print("Kein Sport.")
        else:
            print("Sport!")
    else:
        print("Sport!")
