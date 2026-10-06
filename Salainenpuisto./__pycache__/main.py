from pelaaja import Pelaaja
from paikka import Paikka
from esine import Esine


def lue_tiedosto(tiedostonimi):
    """Lukee tekstin tiedostosta ja palauttaa sen."""
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        return tiedosto.read()


def nayta_ohjeet():
    """Näyttää pelin ohjeet."""
    print(lue_tiedosto("ohjeet.txt"))


def hae_paikka(nimi, paikat):
    """Etsii paikan nimellä ja palauttaa sen."""
    for paikka in paikat:
        if paikka.nimi.lower() == nimi.lower():
            return paikka

    return None


def nayta_paikat(pelaaja):
    """Näyttää nykyisestä paikasta mahdolliset siirtymät."""
    print()
    print("Voit mennä:")

    for paikka in pelaaja.sijainti.yhteydet:
        print("-", paikka.nimi)


def liiku(pelaaja):
    """Kysyy kohteen ja siirtää pelaajan, jos se on sallittu."""
    nayta_paikat(pelaaja)

    kohde = input("Mihin haluat mennä? ")

    for paikka in pelaaja.sijainti.yhteydet:
        if paikka.nimi.lower() == kohde.lower():
            pelaaja.liiku(paikka)
            return True

    print("Et voi mennä tuohon paikkaan tästä.")
    return False


def tallenna_peli(pelaaja):
    """Tallentaa pelaajan tärkeimmät tiedot tiedostoon."""
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(str(pelaaja.ika) + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")
        tiedosto.write(str(pelaaja.pisteet) + "\n")

        esineiden_nimet = []

        for esine in pelaaja.inventaario:
            esineiden_nimet.append(esine.nimi)

        tiedosto.write(",".join(esineiden_nimet))

    print("Peli tallennettu tiedostoon tallennus.txt.")


def lataa_peli(pelaaja, paikat, esineet):
    """Lataa aiemmin tallennetut pelaajan tiedot."""
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.read().splitlines()

        if len(rivit) < 5:
            print("Tallennustiedosto ei ole kunnossa.")
            return False

        pelaaja.nimi = rivit[0]
        pelaaja.ika = int(rivit[1])

        uusi_paikka = hae_paikka(rivit[2], paikat)

        if uusi_paikka is None:
            print("Tallennettua paikkaa ei löytynyt.")
            return False

        pelaaja.sijainti = uusi_paikka
        pelaaja.pisteet = int(rivit[3])
        pelaaja.inventaario = []

        if rivit[4] != "":
            nimet = rivit[4].split(",")

            for nimi in nimet:
                for esine in esineet:
                    if esine.nimi == nimi:
                        pelaaja.inventaario.append(esine)

        print("Peli ladattu.")
        return True

    except FileNotFoundError:
        print("Tallennettua peliä ei löytynyt.")
        return False

    except ValueError:
        print("Tallennustiedostossa on virhe.")
        return False


def tarkista_voitto(pelaaja):
    """Palauttaa True, jos pelaaja on voittanut."""
    if pelaaja.sijainti.nimi != "Portti":
        return False

    if pelaaja.onko_esine("Avain"):
        return True

    return False


def nayta_pisteet(pelaaja):
    """Näyttää pelaajan pisteet."""
    print("Pisteesi ovat:", pelaaja.pisteet)


def pelaa():
    """Näyttää pelin tavoitteen."""
    print()
    print("=== PELIN TAVOITE ===")
    print("Olet hukannut avaimesi.")
    print("Etsi Avain ja palaa sen kanssa Portille.")
    print("Voit valita yhden kolmesta reitistä.")


def luo_peli():
    """Luo pelin paikat, esineet ja pelaajan."""
    print(lue_tiedosto("ohjeet.txt"))

    ika = int(input("Anna ikäsi: "))

    if ika < 12:
        print("Olet alaikäinen. Et voi pelata tätä peliä.")
        return None

    nimi = input("Anna nimesi: ")

    # Luodaan esineet.
    avain = Esine("Avain", 0.1)
    vesipullo = Esine("Vesipullo", 0.5)
    kirja = Esine("Kirja", 0.3)

    # Luodaan paikat.
    portti = Paikka("Portti")
    puisto = Paikka("Puisto", vesipullo)
    kirjasto = Paikka("Kirjasto", kirja)
    pyoraasema = Paikka("Pyöräasema")
    lampi = Paikka("Lampi", avain)

    # Kolme mahdollista reittiä.
    portti.lisaa_yhteys(puisto)
    portti.lisaa_yhteys(kirjasto)
    portti.lisaa_yhteys(pyoraasema)

    kirjasto.lisaa_yhteys(puisto)
    puisto.lisaa_yhteys(lampi)
    pyoraasema.lisaa_yhteys(lampi)

    # Lampi on viimeinen paikka ennen paluuta portille.
    lampi.lisaa_yhteys(portti)

    paikat = [
        portti,
        puisto,
        kirjasto,
        pyoraasema,
        lampi
    ]

    esineet = [
        avain,
        vesipullo,
        kirja
    ]

    pelaaja = Pelaaja(nimi, ika, portti)

    return pelaaja, paikat, esineet


def kaynnista_peli():
    """Käynnistää pelin ja näyttää päävalikon."""
    peli = luo_peli()

    if peli is None:
        return

    pelaaja, paikat, esineet = peli

    print()
    print("Tervetuloa peliin", pelaaja.nimi + "!")
    print("Aloituspaikka:", pelaaja.sijainti.nimi)

    while True:
        print()
        print("==============================")
        print("          PÄÄVALIKKO")
        print("==============================")
        print("pelaa")
        print("pisteet")
        print("ohje")
        print("liiku")
        print("kerää")
        print("inventaario")
        print("paikka")
        print("tallenna")
        print("lataa")
        print("lopeta")
        print("==============================")

        komento = input("Anna komento: ").lower()

        if komento == "pelaa":
            pelaa()

        elif komento == "pisteet":
            nayta_pisteet(pelaaja)

        elif komento == "ohje":
            nayta_ohjeet()

        elif komento == "liiku":
            liiku(pelaaja)

        elif komento == "kerää":
            pelaaja.keraa_esine()

        elif komento == "inventaario":
            pelaaja.nayta_inventaario()

        elif komento == "paikka":
            pelaaja.sijainti.nayta_tiedot()

        elif komento == "tallenna":
            tallenna_peli(pelaaja)

        elif komento == "lataa":
            lataa_peli(pelaaja, paikat, esineet)

        elif komento == "lopeta":
            print("Peli lopetetaan.")
            break

        else:
            print("Tuntematon komento.")

        # Tarkistetaan voitto jokaisen toiminnon jälkeen.
        if tarkista_voitto(pelaaja):
            print()
            print("==============================")
            print("       ONNEKSI OLKOON!")
            print("==============================")
            print("Löysit Avaimen.")
            print("Palasit takaisin Portille.")
            print("Suoritit pelin!")
            print("Pisteesi:", pelaaja.pisteet)
            print("==============================")
            break


kaynnista_peli()