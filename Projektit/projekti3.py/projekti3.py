# projekti 3

ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet alaikäinen.")
else:
    nimi = input("Anna nimesi: ")
    print("Tervetuloa peliin", nimi + "!")

    inventaario = []

    def pelaa():
        print("Peli alkaa! Onnea peliin!")

    def pisteet():
        print("Sinulla on 100 pistettä.")

    def ohje():
        print("Valitse päävalikosta komento kirjoittamalla sen nimi.")

    def lisaa_esine():
        esine = input("Minkä esineen haluat lisätä inventaarioon? ")
        inventaario.append(esine)
        print("Esine lisätty inventaarioon!")

    def nayta_inventaario():
        print("=== INVENTAARIO ===")

        if len(inventaario) == 0:
            print("Inventaario on tyhjä.")
        else:
            for esine in inventaario:
                print("-", esine)

    def salainen():
        print("Löysit salaisen komennon!")

    while True:
        print()
        print("=== PÄÄVALIKKO ===")
        print("pelaa")
        print("pisteet")
        print("ohje")
        print("lisää esine")
        print("inventaario")
        print("salainen")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "lopeta":
            print("Peli lopetetaan.")
            break

        elif komento == "pelaa":
            pelaa()

        elif komento == "pisteet":
            pisteet()

        elif komento == "ohje":
            ohje()

        elif komento == "lisää esine":
            lisaa_esine()

        elif komento == "inventaario":
            nayta_inventaario()

        elif komento == "salainen":
            salainen()

        else:
            print("Tuntematon komento.")

