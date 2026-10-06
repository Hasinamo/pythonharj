from pelaaja import pelaaja
from paikka import paikka
from esine import esine


def lue_tiedosto(nimi):
    with open(nimi, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()


def tallenna(pelaaja1):
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja1.nimi + "\n")
        tiedosto.write(pelaaja1.sijainti.nimi + "\n")
    print("Peli tallennettu!")


ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet alaikäinen.")
else:
    print(lue_tiedosto("intro.txt"))

    nimi = input("Anna nimesi: ")

    avain = esine("Avain", 0.1)
    pullo = esine("Vesipullo", 0.5)

    portti = paikka("Portti")
    puisto = paikka("Puisto", pullo)
    lampi = paikka("Lampi", avain)

    pelaaja1 = pelaaja(nimi, portti)

    while True:
        print()
        print("=== PÄÄVALIKKO ===")
        print("pelaa")
        print("ohje")
        print("liiku")
        print("kerää")
        print("inventaario")
        print("tallenna")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "pelaa":
            print("Etsi avain ja palaa portille!")

        elif komento == "ohje":
            print(lue_tiedosto("ohjeet.txt"))

        elif komento == "liiku":
            print("portti / puisto / lampi")
            kohde = input("Mihin? ")

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

        elif komento == "tallenna":
            tallenna(pelaaja1)

        elif komento == "lopeta":
            print("Peli lopetetaan.")
            break

        else:
            print("Tuntematon komento.")