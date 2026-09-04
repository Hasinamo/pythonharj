ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet alaikäinen.")
else:
    nimi = input("Anna nimesi: ")
    print("Tervetuloa peliin", nimi + "!")

    while True:
        print()
        print("=== PÄÄVALIKKO ===")
        print("pelaa")
        print("pisteet")
        print("ohje")
        print("salainen")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "lopeta":
            print("Peli lopetetaan.")
            break

        elif komento == "pelaa":
            print("Peli alkaa! Onnea peliin!")

        elif komento == "pisteet":
            print("Sinulla on 100 pistettä.")

        elif komento == "ohje":
            print("Valitse päävalikosta komento kirjoittamalla sen nimi.")

        elif komento == "salainen":
            print("Löysit salaisen komennon!")

        else:
            print("Tuntematon komento.")