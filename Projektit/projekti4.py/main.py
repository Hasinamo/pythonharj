from pelaaja import pelaaja
from paikka import paikka
from esine import esine


ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet alaikäinen.")
else:
    nimi = input("Anna nimesi: ")

    avain = esine("Avain", 0.1)
    pullo = esine("Vesipullo", 0.5)

    portti = paikka("Portti")
    puisto = paikka("Puisto", pullo)
    lampi = paikka("Lampi", avain)

    pelaaja1 = pelaaja(nimi, portti)

    def pelaa():
        print("Etsi avain ja palaa portille!")

    def ohje():
        print("Liiku paikkojen välillä ja kerää esineitä.")

    while True:
        print()
        print("=== PÄÄVALIKKO ===")
        print("pelaa")
        print("ohje")
        print("liiku")
        print("kerää")
        print("inventaario")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "pelaa":
            pelaa()

        elif komento == "ohje":
            ohje()

        elif komento == "liiku":
            print("1. portti")
            print("2. puisto")
            print("3. lampi")

            kohde = input("Mihin haluat mennä? ")

            if kohde == "portti":
                pelaaja1.liiku(portti)
            elif kohde == "puisto":
                pelaaja1.liiku(puisto)
            elif kohde == "lampi":
                pelaaja1.liiku(lampi)
            else:
                print("Paikkaa ei löydy.")

        elif komento == "kerää":
            pelaaja1.keraa_esine()

        elif komento == "inventaario":
            pelaaja1.nayta_inventaario()

        elif komento == "lopeta":
            print("Peli lopetetaan.")
            break

        else:
            print("Tuntematon komento.")